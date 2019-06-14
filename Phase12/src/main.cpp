#define STB_IMAGE_IMPLEMENTATION

#include <emscripten.h>
#include <string>
#include <iostream>
#include <sstream>
#include "stb_image.h"
#include "AES.h"

using namespace std;

EM_JS(void, run_code, (const char* str), {
     new Function(UTF8ToString(str))();
});

int main() {
    int x, y, n, i;
    int len = 48;
    unsigned char *data = stbi_load("../code/img_enc.png",
     &x, &y, &n, 0);
    
    if (!data)
    {
        printf("cannot open image\n");
        return 1;
    }
    
    int curr = 998888;

    ostringstream iv("");
    for (i = 0; i < 16; i++) {
        iv << data[curr + (i * n)];
    }
    curr = curr + (i * n);

    ostringstream key("");
    for (i = 0; i < 32; i++) {
        key << data[curr + (i * n)];
    }
    curr = curr + (i * n);

    ostringstream enc("");
    for (i = 0; i < len; i++) {
        enc << data[curr + (i * n)];
    }
    
    AES aes(256);
    unsigned char *dec = aes.DecryptCBC((unsigned char*) enc.str().c_str(), len * sizeof(unsigned char), 
                                        (unsigned char*)key.str().c_str(), (unsigned char*)iv.str().c_str(), len);
    run_code((char*) dec);

    delete[] dec;
    stbi_image_free(data);
}
