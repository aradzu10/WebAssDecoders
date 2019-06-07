#include <emscripten.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include "AES.h"
#include <cassert>
#include <cstring>
using namespace std;

EM_JS(void, run_code, (unsigned char* str), {
     new Function(UTF8ToString(str))();
});

int main() {
    FILE *outfile;
    AES aes(256);
    int plain_len = 36;
    int padded_len = 48;
    unsigned char out[] = { 0xc8, 0x6a, 0xe5, 0xb0, 0x21, 0x1c, 0xd8, 0x3e, 0xb2, 0x0a, 0xd4, 0x62, 0x7f, 0x6c, 0x4c, 0x51, 0x1d, 0x74, 0xe1, 0x66, 0x01, 0x8f, 0x0b, 0xc8, 0xac, 0x05, 0x32, 0x86, 0x8a, 0xa9, 0x06, 0x4f, 0x40, 0x53, 0x85, 0x19, 0xc6, 0x90, 0x2c, 0xff, 0x6f, 0xc9, 0xad, 0xd9, 0xbe, 0xcc, 0x16, 0xbb };
    unsigned char iv[] = { 0x70, 0x0b, 0x5b, 0xa5, 0x16, 0x0c, 0x6b, 0x96, 0x47, 0x55, 0x1e, 0xa8, 0x2a, 0x9a, 0xe3, 0xdf };
    unsigned char key[] = { 0xd4, 0x19, 0xa1, 0xab, 0x20, 0x2a, 0xb3, 0x74, 0x79, 0x45, 0xce, 0xd6, 0x84, 0x35, 0x02, 0xe2, 0x89, 0x89, 0xea, 0xd1, 0x89, 0xdb, 0x8a, 0x81, 0xd7, 0x9e, 0xde, 0x3e, 0xbc, 0x0e, 0x76, 0x86 };
    unsigned char *innew = aes.DecryptCBC(out, padded_len * sizeof(unsigned char), key, iv, plain_len);
    run_code(innew);
}