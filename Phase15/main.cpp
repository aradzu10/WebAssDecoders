#include <stdio.h>
#include <emscripten.h>
#include <string>
#include <emscripten/html5.h>
#include <sstream>
#include <iostream>

using namespace std;

int rnd_f = 0;
int rnd_s = 0;
char code[] = "(function () {alert('Hello there, General Kanobi')})(";

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
    char table[] = {'1', 'a', ')', 'b', 'v', '(', 'd'};

    ostringstream oss("");
    int width = get_window_width(); 
    int index_f = ((e->screenX / (width / 7)) + rnd_f) % 7;
    
    int height = get_window_height(); 
    int index_s = ((e->screenY / (height / 7)) + rnd_s) % 7;
    
    oss << code;
    oss << table[index];
    run_code(oss.str().c_str());
    
    return 0;
}

int main() {
    rnd_f = rand() % 7;
    rnd_s = rand() % 7;
    emscripten_set_mousemove_callback(0, 0, 1, mouse_move);
    return 0;
}