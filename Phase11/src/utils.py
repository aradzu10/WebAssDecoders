import re


def to_snake(name):
    return "_".join(re.findall('([A-Z][a-z0-9]+|[a-z0-9]+)', name)).lower()


class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}'

