#include <emscripten.h>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

EM_JS(void, run_code, (const char* str), {
     eval(UTF8ToString(str));
});

int main() {
    int lenght = 36;
    int chars[] = { 'i', 'o', 'G', ' ', 'a', ',', 'H', 'K', 'r', 'e', 'l', 'h', 't', '(', '\'', 'n', ')', 'b' };
    int numbers[] = {
[4, 10, 9, 8, 12, 13, 14, 6, 9, 10, 10, 1, 3, 12, 11, 9, 8, 9, 5, 3, 2, 9, 15, 9, 8, 4, 10, 3, 7, 4, 15, 1, 17, 0, 14, 16]
};
    ostringstream oss("");
        for (int temp = 0; temp < lenght; temp++)
            oss << table[numbers[temp]];
    run_code(oss.str().c_str());
}