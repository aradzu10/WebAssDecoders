#include <emscripten.h>
#include <string>
#include <iostream>
#include <sstream>
using namespace std;

EM_JS(void, run_code, (const char* str), {
     new Function(UTF8ToString(str))();
});

int main() {
    int lenght = 63;
    int chars[] = { 'a', 'b', 'r', 't', 'K', ')', 'c', ' ', 'o', '(', '}', 'f', 'G', 'i', 'H', 'h', 'e', 'n', 's', '\'', ':', 'P', '6', '{', 'u', 'l', ',' };
    int numbers[] = { 9, 11, 24, 17, 6, 3, 13, 8, 17, 7, 9, 5, 7, 23, 0, 25, 16, 2, 3, 9, 19, 21, 15, 0, 18, 16, 7, 22, 20, 7, 14, 16, 25, 25, 8, 7, 3, 15, 16, 2, 16, 26, 7, 12, 16, 17, 16, 2, 0, 25, 7, 4, 0, 17, 8, 1, 13, 19, 5, 10, 5, 9, 5 };
    ostringstream oss("");
        for (int temp = 0; temp < lenght; temp++)
            oss << chars[numbers[temp]];
    run_code(oss.str().c_str());
}
