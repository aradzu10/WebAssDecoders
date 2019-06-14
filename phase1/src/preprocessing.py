
def generate_main(code):
    return """#include <emscripten.h>

EM_JS(void, run_code, (const char* str), {
    new Function(UTF8ToString(str))();
});

int main() {
    char code[] = \"""" + code + """";
    run_code(code);
    return 0;
}"""


def main():
    code_path = "../code/code.txt"
    with open(code_path) as f:
        code = f.read().replace("\n", "")

    with open("../src/main.cpp", "w") as f:
        f.write(generate_main(code))


if __name__ == '__main__':
    main()
