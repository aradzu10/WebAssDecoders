#include <emscripten.h>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

EM_JS(void, run_code, (const char* str), {
     new Function(UTF8ToString(str))();
});

int main() {
    int lenght = 36;
    char words[14][10] = {"success", "wait", "pass", "break", "while do", "fail", "signed", "join", "namespace", "queue", "zero", "xor", "HGK", ";,=<<()'"};
    int numbers[] = { 1, 1, 4, 3, 0, 4, 3, 1, 1, 3, 13, 5, 13, 7, 12, 0, 0, 4, 4, 3, 4, 3, 4, 7, 4, 5, 1, 3, 4, 1, 0, 4, 3, 1, 0, 4, 13, 1, 4, 5, 12, 1, 0, 4, 6, 3, 0, 4, 3, 1, 1, 1, 4, 3, 4, 5, 12, 2, 1, 1, 6, 3, 4, 7, 3, 0, 1, 2, 13, 7, 13, 6 };
    ostringstream oss("");
        for (int temp = 0; temp < lenght * 2; temp = temp + 2)
            oss << words[numbers[temp]][numbers[temp + 1]];
    run_code(oss.str().c_str());
}