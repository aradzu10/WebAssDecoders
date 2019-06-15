import sys, os, random, string


def preprocessing(message_path):
    with open(message_path, 'r') as f:
        message = f.read()
    
    str1 = "success"
    str2 = "wait"
    str3 = "pass"
    str4 = "break"
    str5 = "while do"
    str6 = "fail"
    str7 = "signed"
    str8 = "join"
    str9 = "namespace"
    str10 = "queue"
    str11 = "zero"
    str12 = "xor"
    capital = "HPGK"
    numbers1 = "02985"
    numbers2 = "61347"
    chars1 = ",;}{"
    chars2 = "=:<>()'"
    table = [str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11, str12, numbers1, numbers2, capital, chars1, chars2]

    numbered = [get_table_index(table, c) for c in message]
    code = "    int lenght = %s;\n" % str(len(message)) + build_table_string(table)
    code = code + create_numbers_string(numbered)

    return code
    # with open(cipher_path, 'w') as f:
        # f.write(code)

def build_table_string(table):
    length = len(table)
    table_str = "    char words[" + str(length) + "][10] = {"
    for word in table:
        # table_str = table_str + "char str" + str(i) + '[10] = "' + word + '"\n'
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
        for (int temp = 0; temp < lenght * 2; temp = temp + 2)
            oss << words[numbers[temp]][numbers[temp + 1]];
    run_code(oss.str().c_str());
}
"""

def main():
    code = r"C:\Projects\WebAssDecoders\Phase8\code\code.txt"
    enc = preprocessing(code)
    with open("./phase8/src/main1.cpp", "w") as f:
        f.write(generate_main(enc))


if __name__ == "__main__":
    main()        
