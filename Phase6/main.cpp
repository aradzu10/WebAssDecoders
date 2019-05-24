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
    int numbers[] = {
        97, 108, 101, 114, 116, 40, 39, 72, 101, 108, 108, 111, 32, 116, 104, 101, 114, 101, 44, 32, 71, 101, 110, 101, 114, 97, 108, 32, 75, 97, 110, 111, 98, 105, 39, 41
    }; 
    ostringstream oss("");
        for (int temp = 0; temp < lenght; temp++)
            oss << (char) numbers[temp];
    run_code(oss.str().c_str());
}