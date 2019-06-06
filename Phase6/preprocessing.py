import sys, os, random, string


def preprocessing(message_path, cipher_path):
    with open(message_path, 'r') as f:
        message = f.read()
    
    # numbered = [str(ord(c)) for c in message]
    chars = list(message)
    table = list(set(chars))
    random.shuffle(table)

    numbered = [table.index(c) for c in message]
    code = "int lenght = %s;\n" % str(len(message)) + \
        "int chars[] = { %s };\n" % build_table_string(table) + \
        "int numbers[] = {\n" + str(numbered) + "\n};"

    with open(cipher_path, 'w') as f:
        f.write(code)

def build_table_string(table):
    bad_chars = ["'", '"']
    formatted = ""
    for c in table:
        if c in bad_chars:
            formatted = formatted + "'\\" + c + "', "
        else:
            formatted = formatted + "'" + c + "', "

    return formatted[:-2]

def main():
    message_path = "C:\Projects\WebAssDecoders\Phase6\code\code.txt"

    folder_name = os.path.dirname(message_path)
    file_name, ext = os.path.splitext(os.path.basename(message_path))
    cipher_path = os.path.join(folder_name, file_name + "_enc" + ext)
    
    preprocessing(message_path, cipher_path)


if __name__ == "__main__":
    main()        
