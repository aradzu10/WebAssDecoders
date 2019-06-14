import sys, os, random, string


def preprocessing(message_path, cipher_path):
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
    capital = "HGK"
    chars = ";,=<<()'"
    table = [str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11, str12, capital, chars]

    numbered = [get_table_index(table, c) for c in message]
    code = "int lenght = %s;\n" % str(len(message)) + build_table_string(table)
    code = code + create_numbers_string(numbered)

    with open(cipher_path, 'w') as f:
        f.write(code)

def build_table_string(table):
    length = len(table)
    table_str = "char words[" + str(length) + "][10] = {"
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
    numbers_str = "int numbers[] = { "
    for tuble in numbered:
        numbers_str = numbers_str + tuble
    numbers_str = numbers_str[:-2]
    numbers_str = numbers_str + " };" 
    return numbers_str


def main():
    message_path = "..\code\code.txt"

    folder_name = os.path.dirname(message_path)
    file_name, ext = os.path.splitext(os.path.basename(message_path))
    cipher_path = os.path.join(folder_name, file_name + "_enc" + ext)
    
    preprocessing(message_path, cipher_path)


if __name__ == "__main__":
    main()        
