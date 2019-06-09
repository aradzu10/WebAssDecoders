#define STB_IMAGE_IMPLEMENTATION

#include <emscripten.h>
#include <string>
#include <iostream>
#include <sstream>
#include "stb_image.h"

using namespace std;

// To compile: add --preload-file code/img_enc.png (or the files you want to use)

EM_JS(void, run_code, (const char* str), {
     new Function(UTF8ToString(str))();
});

int main() {
    int x, y, n;
    unsigned char *data = stbi_load("code/img_enc.png",
     &x, &y, &n, 0);
    
    if (!data)
    {
        printf("cannot open image\n");
        return 1;
    }
    
    int idx = ((int*) data)[0];

    ostringstream oss("");

    int i = 0;
    while (data[idx + (i * n)]) {
        oss << data[idx + (i * n)]; 
        i++;
    }
    
    run_code(oss.str().c_str());

    stbi_image_free(data);
}