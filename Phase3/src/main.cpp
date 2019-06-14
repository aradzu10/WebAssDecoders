#include <emscripten.h>
#include <string>
#include <iostream>
#include "substitution_cipher.h"
using namespace std;

EM_JS(void, run_code, (const char* str), {
    new Function(UTF8ToString(str))();
});

int main() {
    string input("{L<tF;n.tj{fj-PRzB;{0beP!zj(rj\\zRR.j;ezBz_j8ztzBPRj}Pt. n0f,f{f");
    string org_alph("e1.QtA}BE`qXyf0->dRbY('K]j,_I[;J7Cs5DuF6H3W9Gi*~L z&^l?#c/T${2=p%NhV@Prv)Znam\\O\"8kx:<o+SMU|4gw!");
    string key_alph("zI`3;y,TW5Gi$LEmoVu /{0}%9_@xpv]DS!7w<~q\\(a48n+^cjH?#Rh&FJA>-\"ZYX)eMCbBlfdtP|1*g'N[rK.U2Os:Q6k=");
    string code("");
    SubstitutionCipher::decrypt(input, org_alph, key_alph, code);
    run_code(code.c_str());
}
