import os
import sys
import urllib2


def preprocessing(message_path, cipher_path):
    with open(message_path, 'r') as f:
        message = f.read()

    data = urllib2.urlopen("https://code.jquery.com/jquery-3.4.1.min.js").read()

    tabel_idxs = []
    already_found = 0
    current_find = message
    while current_find != "":
        idx = data.find(current_find)
        if idx != -1:
            tabel_idxs.append((idx, len(current_find)))
            already_found += len(current_find)
            current_find = message[already_found:]
        else:
            current_find = current_find[:-1]
    
    if already_found != len(message):
        raise Exception("Couldn't find all chars")

    code = "int lenght = %s;\n" % str(len(tabel_idxs)) + \
           "int *idxs_table = new int[2*%s];\n" % str(len(tabel_idxs)) + \
           "".join("idxs_table[%s] = %s;\tidxs_table[%s + %s] = %s;\n"
                   % (str(i), str(idx[0]), str(len(tabel_idxs)), str(i), str(idx[1]))
                   for i, idx in enumerate(tabel_idxs)) + \
           "delete [] idxs_table;\n"

    with open(cipher_path, 'w') as f:
        f.write(code)


def main():
    message_path = r"C:\Users\arzulti\Project\WebAssDecoders\real_mallware_do_not_run\the_one_do_not_run.js.txt"

    folder_name = os.path.dirname(message_path)
    file_name, ext = os.path.splitext(os.path.basename(message_path))
    cipher_path = os.path.join(folder_name, file_name + "_enc" + ext)
    
    preprocessing(message_path, cipher_path)


if __name__ == "__main__":
    main()        
