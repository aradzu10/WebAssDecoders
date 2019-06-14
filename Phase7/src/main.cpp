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
    int* numbers = new int[lenght];
    numbers[0] = 11;
    numbers[1] = 3;
    numbers[2] = 8;
    numbers[3] = 12;
    numbers[4] = 10;
    numbers[5] = 14;
    numbers[6] = 0;
    numbers[7] = 17;
    numbers[8] = 8;
    numbers[9] = 3;
    numbers[10] = 3;
    numbers[11] = 2;
    numbers[12] = 15;
    numbers[13] = 10;
    numbers[14] = 6;
    numbers[15] = 8;
    numbers[16] = 12;
    numbers[17] = 8;
    numbers[18] = 9;
    numbers[19] = 15;
    numbers[20] = 13;
    numbers[21] = 8;
    numbers[22] = 16;
    numbers[23] = 8;
    numbers[24] = 12;
    numbers[25] = 11;
    numbers[26] = 3;
    numbers[27] = 15;
    numbers[28] = 1;
    numbers[29] = 11;
    numbers[30] = 16;
    numbers[31] = 2;
    numbers[32] = 4;
    numbers[33] = 5;
    numbers[34] = 0;
    numbers[35] = 7;


    ostringstream oss("");
    for (int temp = 0; temp < lenght; temp++)
        oss << (char) numbers[temp];
    run_code(oss.str().c_str());

    delete [] numbers;
}