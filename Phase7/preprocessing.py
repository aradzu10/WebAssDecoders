import sys, os, random, string

def preprocessing(message_path, cipher_path):
    with open(message_path, 'r') as f:
        message = f.read()
        
    chars = list(message)
    table = list(set(chars))
    random.shuffle(table)
    numbered = [table.index(c) for c in message]

    init_array = ["numbers[%s] = %s;\n" % (i, c) for i, c in enumerate(numbered)] 

    code = "int lenght = " + str(len(numbered)) + ";\n" + \
         "int* numbers = new int[lenght];\n" + "".join(init_array)

    with open(cipher_path, 'w') as f:
        f.write(code)


def main():
    message_path = "C:\Projects\WebAssDecoders\Phase7\code\code.txt"

    folder_name = os.path.dirname(message_path)
    file_name, ext = os.path.splitext(os.path.basename(message_path))
    cipher_path = os.path.join(folder_name, file_name + "_enc" + ext)
    
    preprocessing(message_path, cipher_path)


if __name__ == "__main__":
    main()        
