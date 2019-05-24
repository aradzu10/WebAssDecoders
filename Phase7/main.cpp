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
    int* numbers = new int[lenght];
    numbers[0] = 97;
    numbers[1] = 108;
    numbers[2] = 101;
    numbers[3] = 114;
    numbers[4] = 116;
    numbers[5] = 40;
    numbers[6] = 39;
    numbers[7] = 72;
    numbers[8] = 101;
    numbers[9] = 108;
    numbers[10] = 108;
    numbers[11] = 111;
    numbers[12] = 32;
    numbers[13] = 116;
    numbers[14] = 104;
    numbers[15] = 101;
    numbers[16] = 114;
    numbers[17] = 101;
    numbers[18] = 44;
    numbers[19] = 32;
    numbers[20] = 71;
    numbers[21] = 101;
    numbers[22] = 110;
    numbers[23] = 101;
    numbers[24] = 114;
    numbers[25] = 97;
    numbers[26] = 108;
    numbers[27] = 32;
    numbers[28] = 75;
    numbers[29] = 97;
    numbers[30] = 110;
    numbers[31] = 111;
    numbers[32] = 98;
    numbers[33] = 105;
    numbers[34] = 39;
    numbers[35] = 41;

    ostringstream oss("");
        for (int temp = 0; temp < lenght; temp++)
            oss << (char) numbers[temp];
    run_code(oss.str().c_str());
}