#include <emscripten.h>

EM_JS(void, run_code, (const char* str), {
    eval(UTF8ToString(str));
});

int main() {

}