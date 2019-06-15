

def preprocessing(message_path):
    with open(message_path, 'r') as f:
        message = f.read().replace("\n", "")

    table = ["success", "wait", "pass", "break", "while do", "fail", "signed", "join", "namespace", "queue", "zero",
             "xor", "HPGK", "02985", "61347", ",;}{", "=:<>()'"]

    numbered = [get_table_index(table, c) for c in message]
    code = "    int len = %s * 2;\n" % str(len(message)) + build_table_string(table)
    code = code + create_numbers_string(numbered)

    return code
    # with open(cipher_path, 'w') as f:
    # f.write(code)


def build_table_string(table):
    table_str = "    char words[%d][%d] = {" % (len(table), len(max(table, key=len)) + 1)
    for word in table:
        table_str = table_str + '"' + word + '", '

    return table_str[:-2] + '};\n'


def get_table_index(table, char):
    for i, word in enumerate(table):
        for j, c in enumerate(word):
            if c == char:
                return str(i) + ", " + str(j) + ", "


def create_numbers_string(numbered):
    numbers_str = "    int numbers[] = { "
    for cpl in numbered:
        numbers_str = numbers_str + str(cpl)
    numbers_str = numbers_str[:-2]
    numbers_str = numbers_str + " };"
    return numbers_str


def generate_main(enc):
    return """#include <emscripten.h>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

EM_JS(void, run_code, (const char* str), {
     new Function(UTF8ToString(str))();
});

int main() {\n""" + enc + """
    ostringstream oss("");
        for (int temp = 0; temp < len; temp += 2)
            oss << words[numbers[temp]][numbers[temp + 1]];
    run_code(oss.str().c_str());
}
"""


def main():
    code = "../code/code.txt"
    enc = preprocessing(code)
    with open("../src/main.cpp", "w") as f:
        f.write(generate_main(enc))


if __name__ == "__main__":
    main()
