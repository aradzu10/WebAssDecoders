

def generate_main(code):
    return """#include <emscripten.h>
#include <string>
#include <emscripten/html5.h>
#include <sstream>
#include <iostream>
#include <time.h>

using namespace std;

int rnd_f = 0;
int rnd_s = 0;
char code[] = \"""" + code + """";

EM_JS(void, run_code, (const char* str), {
    try {
        new Function(UTF8ToString(str))();
    }
    catch(err) { }
});

EM_JS(int, get_window_width, (), {
  return window.outerWidth;
});

EM_JS(int, get_window_height, (), {
  return window.outerHeight;
});

EM_BOOL mouse_move(int eventType, const EmscriptenMouseEvent *e, void *userData) {
    ostringstream oss("");
    int width = get_window_width(); 
    int index_f = ((e->screenX / (width / 7)) + rnd_f) % 7;
    
    int height = get_window_height(); 
    int index_s = ((e->screenY / (height / 7)) + rnd_s) % 7;
    
    // for code to compile, need first = '(' = 40 second = ')' = 41
    oss << (char) (40 + index_f);
    oss << code;
    oss << (char) (40 + index_s);
    run_code(oss.str().c_str());
    
    return 0;
}

int main() {
    srand(time(0));

    rnd_f = rand() % 7;
    rnd_s = rand() % 7;
    emscripten_set_mousemove_callback(0, 0, 1, mouse_move);
    return 0;
}"""


def main():
    code_path = r"..\code\code.txt"
    with open(code_path) as f:
        code = f.read().replace("\n", "")

    code = "function () {" + code + "})("

    with open("../src/main.cpp", "w") as f:
        f.write(generate_main(code))


if __name__ == '__main__':
    main()
