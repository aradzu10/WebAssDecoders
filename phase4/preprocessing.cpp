#include <stdio.h>
#include <iostream>
#include <fstream>
#include "AES.h"
#include <cassert>
#include <cstring>


using namespace std;

void CBC()
{
  FILE *outfile;
  AES aes(256);
  int plain_len = 36;
  unsigned char plain[] = { 0x61, 0x6c, 0x65, 0x72, 0x74, 0x28, 0x27, 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x74, 0x68, 0x65, 0x72, 0x65, 0x2c, 0x20, 0x47, 0x65, 0x6e, 0x65, 0x72, 0x61, 0x6c, 0x20, 0x4b, 0x61, 0x6e, 0x6f, 0x62, 0x69, 0x27, 0x29 };
  unsigned char iv[] = { 0x41, 0x64, 0xcd, 0xf1, 0x2c, 0x8d, 0xbb, 0x77, 0x66, 0x22, 0x3c, 0x0d, 0xdd, 0x0f, 0xfd, 0x4e };
  unsigned char key[] = { 0x55, 0xd0, 0x32, 0x78, 0x16, 0x32, 0x47, 0x4e, 0xb8, 0x66, 0x69, 0x66, 0x08, 0x1d, 0x66, 0xb9, 0xdf, 0xba, 0x14, 0x0f, 0x96, 0xdf, 0x70, 0x52, 0xbf, 0x87, 0xfe, 0xdf, 0x7d, 0xcd, 0x21, 0xd6 };

  unsigned int len;
  unsigned char *out = aes.EncryptCBC(plain, plain_len * sizeof(unsigned char), key, iv, len);
  unsigned char *innew = aes.DecryptCBC(out, len * sizeof(unsigned char), key, iv, plain_len);
  assert(!memcmp(innew, plain, plain_len * sizeof(unsigned char)));
  cout << "Test CBC [OK]" << endl;

  outfile = fopen ("C:/Projects/WebAssDecoders/phase4/code/encrypted.txt", "wb");
  fwrite (out , sizeof(unsigned char), len, outfile);
  // fwrite (innew , sizeof(unsigned char), len, outfile);
  // fwrite ('\n\n' , sizeof(unsigned char), 1, outfile);
  // fwrite (innew , sizeof(unsigned char), 16, outfile);
  fclose (outfile);

  delete[] out;
  delete[] innew;
}

// int main()
// {
  // CBC();
  // return 0;
// }