#include <emscripten.h>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

EM_JS(void, run_code, (const char* str), {
     new Function(UTF8ToString(str))();
});

int main() {
    int len = 63;
    int* numbers = new int[len];
    
    char table[] = { '{', 'e', '7', 'l', ',', 'H', 'G', 't', 'c', 'f', 'K', 'n', 'b', '}', '\'', 'P', 's', 'o', 'r', 'u', ')', 'h', ' ', '(', ':', 'i', 'a' };
    
    numbers[0] = 23;
	numbers[1] = 9;
	numbers[2] = 19;
	numbers[3] = 11;
	numbers[4] = 8;
	numbers[5] = 7;
	numbers[6] = 25;
	numbers[7] = 17;
	numbers[8] = 11;
	numbers[9] = 22;
	numbers[10] = 23;
	numbers[11] = 20;
	numbers[12] = 22;
	numbers[13] = 0;
	numbers[14] = 26;
	numbers[15] = 3;
	numbers[16] = 1;
	numbers[17] = 18;
	numbers[18] = 7;
	numbers[19] = 23;
	numbers[20] = 14;
	numbers[21] = 15;
	numbers[22] = 21;
	numbers[23] = 26;
	numbers[24] = 16;
	numbers[25] = 1;
	numbers[26] = 22;
	numbers[27] = 2;
	numbers[28] = 24;
	numbers[29] = 22;
	numbers[30] = 5;
	numbers[31] = 1;
	numbers[32] = 3;
	numbers[33] = 3;
	numbers[34] = 17;
	numbers[35] = 22;
	numbers[36] = 7;
	numbers[37] = 21;
	numbers[38] = 1;
	numbers[39] = 18;
	numbers[40] = 1;
	numbers[41] = 4;
	numbers[42] = 22;
	numbers[43] = 6;
	numbers[44] = 1;
	numbers[45] = 11;
	numbers[46] = 1;
	numbers[47] = 18;
	numbers[48] = 26;
	numbers[49] = 3;
	numbers[50] = 22;
	numbers[51] = 10;
	numbers[52] = 26;
	numbers[53] = 11;
	numbers[54] = 17;
	numbers[55] = 12;
	numbers[56] = 25;
	numbers[57] = 14;
	numbers[58] = 20;
	numbers[59] = 13;
	numbers[60] = 20;
	numbers[61] = 23;
	numbers[62] = 20;
    
    
    ostringstream oss("");
    for (int temp = 0; temp < len; temp++)
        oss << (char) table[numbers[temp]];
    run_code(oss.str().c_str());

    delete [] numbers;
}
