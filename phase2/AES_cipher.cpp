#include <emscripten.h>
#include <Crypto++.h>

EM_JS(void, run_code, (const char* str), {
  eval(UTF8ToString(str));
});

int main() {
  CFB_Mode<AES>::Decryption cfbDecryption(key, key.size(), iv);
  cfbDecryption.ProcessData(plainText, plainText, messageLen);

  char code[] = "alert('hello');";
  run_code(code);
  return 0;
}