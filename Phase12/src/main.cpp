#define STB_IMAGE_IMPLEMENTATION

// #include <emscripten.h>
#include <string>
#include <iostream>
#include <sstream>
#include "stb_image.h"
#include "AES.h"

using namespace std;

// EM_JS(void, run_code, (const char* str), {
//      new Function(UTF8ToString(str))();
// });

int main() {
    int x, y, n;
    unsigned char *data = stbi_load("../code/img_enc.png",
     &x, &y, &n, 0);
    
    if (!data)
    {
        printf("cannot open image\n");
        return 1;
    }
    
    int idx = ((int*) data)[0];

    int i = 0;
    ostringstream iv("");
    while (data[idx + (i * n)]) {
        iv << data[idx + (i * n)]; 
        i++;
    }

    i++;
    ostringstream key("");
    while (data[idx + (i * n)]) {
        key << data[idx + (i * n)]; 
        i++;
    }

    i++;
    ostringstream enc("");
    while (data[idx + (i * n)]) {
        enc << data[idx + (i * n)]; 
        i++;
    }
    
    int len = enc.str().length();
    AES aes(256);
    unsigned char *dec = aes.DecryptCBC((unsigned char*) enc.str().c_str(), len * sizeof(unsigned char), 
                                        (unsigned char*)key.str().c_str(), (unsigned char*)iv.str().c_str(), len);
    // run_code((char*) dec);

    delete[] dec;
    stbi_image_free(data);
}