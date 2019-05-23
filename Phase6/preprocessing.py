import sys, os, random, string


def preprocessing(message_path, cipher_path):
    with open(message_path, 'r') as f:
        message = f.read()
    
    numbered = [str(ord(c)) for c in message]
    
    code = "int lenght = " + str(len(numbered)) + \
         ";\nint numbers[] = {\n" + ", ".join(numbered) + "\n}; "

    with open(cipher_path, 'w') as f:
        f.write(code)


def main():
    if len(sys.argv) != 2:
        return

    message_path = sys.argv[-1]

    folder_name = os.path.dirname(message_path)
    file_name, ext = os.path.splitext(os.path.basename(message_path))
    cipher_path = os.path.join(folder_name, file_name + "_enc" + ext)
    
    preprocessing(message_path, cipher_path)


if __name__ == "__main__":
    main()        
