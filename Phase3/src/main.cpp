#include <emscripten.h>
#include <string>
#include <iostream>
#include "substitution_cipher.h"
using namespace std;

EM_JS(void, run_code, (const char* str), {
    new Function(UTF8ToString(str))();
});

int main() {
    string input("i-C~jTe+~si`sq*HxpTiw}h*fxsj.saxHH+sThxpxUsgx~xp*HsF*~+Xew`z`i`");
    string org_alph("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ ");
    string key_alph("*Xj:x-cheP HY~+]rpfTC_M$/JdBO=uvga\"SF!<VA}(NDQ{%n,'tLbI)>lwi`Z^UoR?.mk[K#|;\\EG@Wq&zys");
    string code("");
    SubstitutionCipher::decrypt(input, org_alph, key_alph, code);
    run_code(code.c_str());
}
