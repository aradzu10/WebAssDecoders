#include <emscripten.h>
#include <string>
#include <iostream>
#include "substitution_cipher.h"
using namespace std;

EM_JS(void, run_code, (const char* str), {
     eval(UTF8ToString(str));
});

int main() {
    string input("$.:;fC>?:..sWfw:;:rW#:e:;$.WN$esHF>X");
    string org_alph("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ ");
    string key_alph("$Hiv:qAwFLR.%esYE;afOKoZ-pg\"@B*d#?UxNh`!(j^VS{nTz[l|~\\QJ+t>CX Dr)PyGu_bM&=</,kI'cm}]W");
    string code("");
	SubstitutionCipher::decrypt(input, org_alph, key_alph, code);
    run_code(code.c_str());
}