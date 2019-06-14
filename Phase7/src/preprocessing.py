import os
import random


def generate_main(init_array, table):
    return """#include <emscripten.h>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

EM_JS(void, run_code, (const char* str), {
     new Function(UTF8ToString(str))();
});

int main() {
    int len = %d;
    int* numbers = new int[len];
    
    char table[] = { %s };
    
    %s
    
    
    ostringstream oss("");
    for (int temp = 0; temp < len; temp++)
        oss << (char) numbers[temp];
    run_code(oss.str().c_str());

    delete [] numbers;
}
""" % (len(init_array), ", ".join(table), "\n\t".join(init_array))


def init_numbers(message_path):
    with open(message_path, 'r') as f:
        message = f.read()

    chars = list(message)
    table = list(set(chars))
    random.shuffle(table)
    numbered = [table.index(c) for c in message]

    init_array = ["numbers[%s] = %s;" % (i, c) for i, c in enumerate(numbered)]

    bad_chars = ["'", '"']
    table = ["'%s'" % (('\\%s' % c) if c in bad_chars else c) for c in table]

    return table, init_array


def main():
    message_path = r"..\code\code.txt"

    table, init_array = init_numbers(message_path)
    with open(r"..\src\main.cpp", "w") as f:
        f.write(generate_main(init_array, table))


if __name__ == "__main__":
    main()
