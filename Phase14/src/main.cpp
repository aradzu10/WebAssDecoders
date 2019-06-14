#include <emscripten.h>
#include <string>
#include <emscripten/html5.h>
#include <sstream>
#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

int rnd_width = 0;
int rnd_height = 0;
char code[] = "alert('Phase 14: Hello there, General Kanobi')";

EM_JS(void, run_code, (const char* str), {
    new Function(UTF8ToString(str))();
});

EM_JS(int, get_window_width, (), {
  return window.innerWidth;
});

EM_JS(int, get_window_height, (), {
  return window.innerHeight;
});

EM_BOOL mouse_move(int eventType, const EmscriptenMouseEvent *e, void *userData) {

  if (abs(e->clientX - rnd_width) <= 50 && abs(e->clientY - rnd_height) <= 50) {
      run_code(code);
  }
  return 0;
}

int main() {
    srand(time(0));

    int width = get_window_width() - 100;
    int height = get_window_height() - 100;
    rnd_width = (rand() % width) + 50;
    rnd_height = (rand() % height) + 50;
    emscripten_set_mousemove_callback(0, 0, 1, mouse_move);
    return 0;
}
