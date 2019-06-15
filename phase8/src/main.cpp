#include <emscripten.h>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

EM_JS(void, run_code, (const char* str), {
     new Function(UTF8ToString(str))();
});

int main() {
    int len = 45 * 2;
    char words[17][10] = {"success", "wait", "pass", "break", "while do", "fail", "signed", "join", "namespace", "queue", "zero", "xor", "HPGK", "02985", "61347", ",;}{", "=:<>()'"};
    int numbers[] = { 1, 1, 4, 3, 0, 4, 3, 1, 1, 3, 16, 4, 16, 6, 12, 1, 4, 1, 1, 1, 0, 0, 0, 4, 4, 5, 13, 3, 16, 1, 4, 5, 12, 0, 0, 4, 4, 3, 4, 3, 4, 7, 4, 5, 1, 3, 4, 1, 0, 4, 3, 1, 0, 4, 15, 0, 4, 5, 12, 2, 0, 4, 6, 3, 0, 4, 3, 1, 1, 1, 4, 3, 4, 5, 12, 3, 1, 1, 6, 3, 4, 7, 3, 0, 1, 2, 16, 6, 16, 5 };
    ostringstream oss("");
        for (int temp = 0; temp < len; temp += 2)
            oss << words[numbers[temp]][numbers[temp + 1]];
    run_code(oss.str().c_str());
}
