def generate_main(code_path):
    return """#include <stdio.h>
#include <string>
#include <emscripten.h>
#include <sstream>
#include <iostream>

using namespace std;

EM_JS(void, run_code, (const char *str), {
    new Function(UTF8ToString(str))();
});

int main()
{

    ostringstream oss("");
    FILE *file = fopen(\"""" + code_path + """", "rb");

    if (!file)
    {
        printf("cannot open file\\n");
        return 1;
    }

    char c = fgetc(file);
    while (!feof(file))
    {
        oss << c;
        c = fgetc(file);
    }
    
    run_code(oss.str().c_str());
    
    return 0;
}
"""


if __name__ == "__main__":
    code_path = "code/code.txt"

    if code_path != "code/code.txt":
        print("Warning! you change the code path. "
              "you need to change the --preload-file flag in build/build_and_run.bat")

    with open("../src/main.cpp", "w") as f:
        f.write(generate_main("code/code.txt"))
