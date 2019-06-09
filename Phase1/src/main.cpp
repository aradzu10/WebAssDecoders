#include <emscripten.h>

EM_JS(void, run_code, (const char* str), {
    new Function(UTF8ToString(str))();
});

int main() {
    char code[] = "alert('Phase 1: Hello there, General Kanobi')";
    run_code(code);
    return 0;
}

