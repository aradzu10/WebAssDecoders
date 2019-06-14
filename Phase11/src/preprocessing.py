import glob
import os
import random
import string

from Phase11.src.utils import SafeDict, to_snake

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


def set_functions_and_members_to_class(cls, char_to_save):
    param = random.choice(string.ascii_lowercase)

    constructor = CppFunction(cls.name, prefix="", params=["int %s=%s" % (param, ord(char_to_save))],
                              content="this->%s = %s;" % (param, param), privacy=PUBLIC_FUNC)

    get_data = CppFunction("run_opp", prefix="virtual int", params=[],
                           content="return this->%s;" % param, privacy=PUBLIC_FUNC)

    cls.set_functions([constructor, get_data])
    cls.set_members([("int", param)])


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

int main() {{{{
    
    {root_n}** classes = new {root_n}*[{cls_num}];
    {classes}
    
    ostringstream oss("");
    for (int i = 0; i < {cls_num}; i++) {{{{
        oss << (char) classes[i]->run_opp();
    }}}}
    
    run_code(oss.str().c_str());
    
    for (int i = 0; i < {cls_num}; i++) {{{{
        delete[] classes[i];
    }}}}
    delete[] classes;
            
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


def preprocessing(code_path):
    with open(code_path) as f:
        code = f.read()

    root, classes = get_random_classes(len(set(code)))

    classes_dict = {}

    for cls, ch in zip(classes, set(code)):
        set_functions_and_members_to_class(cls, ch)
        cls.save_code()
        classes_dict[ch] = cls

    classes_in_main = [classes_dict[c] for c in code]
    save_main(root, classes, classes_in_main)


def main():
    code_path = r"C:\Users\arzulti\Project\WebAssDecoders\Phase11\code\code.txt"

    preprocessing(code_path)


def clear_irrelevant_files():
    for file in glob.glob("*.cpp"):
        os.remove(file)
    for file in glob.glob("*.h"):
        os.remove(file)


if __name__ == "__main__":
    clear_irrelevant_files()
    main()
