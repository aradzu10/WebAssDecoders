// #include "emscripten.h"
#include <string>
#include <iostream>
#include "substitution_cipher.h"
using namespace std; 

// EM_JS(void, run_code, (const char* str), {
    //  eval(UTF8ToString(str));
// });

int main() {
	string alpha;
    string key;
    string input;
    string code;
    cout << "Hello";
	SubstitutionCipher::decrypt(input, key, alpha, code);
}