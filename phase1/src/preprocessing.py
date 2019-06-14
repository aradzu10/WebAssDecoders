def add_includes(code):
    code = code + "#include <emscripten.h>\n"
    code = code + "\n"
    return code

def add_js(code):
    code = code + "EM_JS(void, run_code, (const char* str), {\n"
    code = code + "    new Function(UTF8ToString(str))();\n"
    code = code + "});\n"
    code = code + "\n"
    return code

def add_main(code):
    code = code + "int main() {\n"
    code = code + "    char code[] = \"alert('Phase 1: Hello there, General Kanobi')\";\n"
    code = code + "    run_code(code);\n"
    code = code + "    return 0;\n"
    code = code + "}\n"
    code = code + "\n"
    return code
    

def create_main(main_path):
    code = ""
    code = add_includes(code)
    code = add_js(code)
    code = add_main(code)
    with open(main_path, 'w') as f:
        f.write(code)


def main():
    message_path = "..\src\main.cpp"
    create_main(message_path)


if __name__ == "__main__":
    main()