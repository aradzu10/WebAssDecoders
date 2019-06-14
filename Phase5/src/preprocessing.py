def generate_main():
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
    FILE *file = fopen("code/code.txt", "rb");

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
    with open("./phase5/src/main1.cpp", "w") as f:
        f.write(generate_main())
