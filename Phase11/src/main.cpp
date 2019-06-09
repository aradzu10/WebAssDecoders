#include <emscripten.h>
#include <string>
#include <iostream>
#include <sstream>
#include "cfu_21.h"
#include "cfu_23.h"
#include "cfu_14.h"
#include "cfu_15.h"
#include "cfu_7.h"
#include "cfu_16.h"
#include "cfu_3.h"
#include "cfu_25.h"
#include "cfu_22.h"
#include "cfu_13.h"
#include "cfu_2.h"
#include "cfu_9.h"
#include "cfu_18.h"
#include "cfu_11.h"
#include "cfu_1.h"
#include "cfu_4.h"
#include "cfu_17.h"
#include "cfu_8.h"
#include "cfu_20.h"
#include "cfu_6.h"
#include "cfu_12.h"
#include "cfu_24.h"
#include "cfu_19.h"
#include "cfu_10.h"
#include "cfu_5.h"
#include "cfu_27.h"
#include "cfu_26.h"

using namespace std;

EM_JS(void, run_code, (const char* str), {
    new Function(UTF8ToString(str))();
});

int main() {
    
    Cfu_21** classes = new Cfu_21*[64];
    classes[0] = new Cfu_27();
	classes[1] = new Cfu_17();
	classes[2] = new Cfu_10();
	classes[3] = new Cfu_5();
	classes[4] = new Cfu_7();
	classes[5] = new Cfu_23();
	classes[6] = new Cfu_13();
	classes[7] = new Cfu_22();
	classes[8] = new Cfu_5();
	classes[9] = new Cfu_11();
	classes[10] = new Cfu_27();
	classes[11] = new Cfu_25();
	classes[12] = new Cfu_11();
	classes[13] = new Cfu_20();
	classes[14] = new Cfu_14();
	classes[15] = new Cfu_9();
	classes[16] = new Cfu_2();
	classes[17] = new Cfu_4();
	classes[18] = new Cfu_23();
	classes[19] = new Cfu_27();
	classes[20] = new Cfu_16();
	classes[21] = new Cfu_24();
	classes[22] = new Cfu_6();
	classes[23] = new Cfu_14();
	classes[24] = new Cfu_1();
	classes[25] = new Cfu_2();
	classes[26] = new Cfu_11();
	classes[27] = new Cfu_21();
	classes[28] = new Cfu_21();
	classes[29] = new Cfu_18();
	classes[30] = new Cfu_11();
	classes[31] = new Cfu_12();
	classes[32] = new Cfu_2();
	classes[33] = new Cfu_9();
	classes[34] = new Cfu_9();
	classes[35] = new Cfu_22();
	classes[36] = new Cfu_11();
	classes[37] = new Cfu_23();
	classes[38] = new Cfu_6();
	classes[39] = new Cfu_2();
	classes[40] = new Cfu_4();
	classes[41] = new Cfu_2();
	classes[42] = new Cfu_8();
	classes[43] = new Cfu_11();
	classes[44] = new Cfu_26();
	classes[45] = new Cfu_2();
	classes[46] = new Cfu_5();
	classes[47] = new Cfu_2();
	classes[48] = new Cfu_4();
	classes[49] = new Cfu_14();
	classes[50] = new Cfu_9();
	classes[51] = new Cfu_11();
	classes[52] = new Cfu_19();
	classes[53] = new Cfu_14();
	classes[54] = new Cfu_5();
	classes[55] = new Cfu_22();
	classes[56] = new Cfu_15();
	classes[57] = new Cfu_13();
	classes[58] = new Cfu_16();
	classes[59] = new Cfu_25();
	classes[60] = new Cfu_3();
	classes[61] = new Cfu_25();
	classes[62] = new Cfu_27();
	classes[63] = new Cfu_25();
    
    ostringstream oss("");
    for (int i = 0; i < 64; i++) {
        oss << (char) classes[i]->run_opp();
    }
    
    run_code(oss.str().c_str());
    
    for (int i = 0; i < 64; i++) {
        delete[] classes[i];
    }
    delete[] classes;
            
    return 0;
}
