#include <stdio.h>
#include <emscripten.h>
#include <string>
#include <emscripten/html5.h>
#include <sstream>
#include <iostream>

using namespace std;

EM_JS(void, run_code, (const char* str), {
    new Function(UTF8ToString(str))();
});

int main() {
  
  ostringstream oss("");

  FILE *file = fopen("../Phase5/code/code.txt", "rb");
  if (!file) {
    printf("cannot open file\n");
    return 1;
  }
  do {
    char c = fgetc(file);
    oss << c;
  } while(c != EOF);
  fclose (file);

  run_code(oss.str().c_str());

  return 0;
}