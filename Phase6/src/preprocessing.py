import os
import random


def preprocessing(message_path):
    with open(message_path, 'r') as f:
        message = f.read()
    
    # numbered = [str(ord(c)) for c in message]
    chars = list(message)
    table = list(set(chars))
    random.shuffle(table)

    numbered = [table.index(c) for c in message]
    length = "int lenght = %s;" % str(len(message))
    chars = "int chars[] = { %s };" % build_table_string(table)
    numbers = "int numbers[] = { " + ", ".join(str(n) for n in numbered) + " };"
    return length, chars, numbers

    # with open(cipher_path, 'w') as f:
        # f.write(code)


def build_table_string(table):
    bad_chars = ["'", '"']
    formatted = ""
    for c in table:
        if c in bad_chars:
            formatted = formatted + "'\\" + c + "', "
        else:
            formatted = formatted + "'" + c + "', "

    return formatted[:-2]


def main():
    message_path = r"..\code\code.txt"
    preprocessing(message_path)


def generate_main(length, chars, numbers):
    return """#include <emscripten.h>
#include <string>
#include <iostream>
#include <sstream>
using namespace std;

EM_JS(void, run_code, (const char* str), {
     new Function(UTF8ToString(str))();
});

int main() {
    """ + length + """
    """ + chars + """
    """ + numbers + """
    ostringstream oss("");
        for (int temp = 0; temp < lenght; temp++)
            oss << chars[numbers[temp]];
    run_code(oss.str().c_str());
}
"""


if __name__ == "__main__":
    code = r"C:\Projects\WebAssDecoders\Phase6\code\code.txt"
    length, chars, numbers = preprocessing(code)
    with open("./phase6/src/main1.cpp", "w") as f:
        f.write(generate_main(length, chars, numbers))


if __name__ == "__main__":
    main()        
