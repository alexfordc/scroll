__author__ = 'ict'

import pprint
import re

from service.client import Client

type_offset = 0
size_offset = 1
lock_offset = 2

name_title = "name"
type_title = "type"
size_title = "size"
lock_title = "lock"


def normal_size(size):
    if size < 1024:
        return str(size) + "B"
    elif 1024 < size < 1024 * 1024:
        str_size = str(size / 1024)
        return str_size[: str_size.find(".") + 3] + "K"
    else:
        str_size = str(size / (1024 * 1024))
        return str_size[: str_size.find(".") + 3] + "M"


def print_list(var_dict):
    name_len = len(name_title)
    type_len = len(type_title)
    size_len = len(size_title)
    lock_len = len(lock_title)
    for name, attr in var_dict.items():
        if len(str(name)) > name_len:
            name_len = len(str(name))
        if len(str(attr[type_offset])) > type_len:
            type_len = len(str(attr[type_offset]))
        if len(normal_size(attr[size_offset])) > size_len:
            size_len = len(normal_size(attr[size_offset]))
        if len(str(attr[lock_offset])) > lock_len:
            lock_len = len(str(attr[lock_offset]))
    print("+-" + "-" * name_len + "-+-" + "-" * type_len + "-+-" + "-" * size_len + "-+-" + "-" * lock_len + "-+")
    print("| " + name_title + " " * (name_len - len(name_title)), end="")
    print(" | " + type_title + " " * (type_len - len(type_title)), end="")
    print(" | " + size_title + " " * (size_len - len(size_title)), end="")
    print(" | " + lock_title + " " * (lock_len - len(lock_title)) + " |")
    print("+-" + "-" * name_len + "-+-" + "-" * type_len + "-+-" + "-" * size_len + "-+-" + "-" * lock_len + "-+")
    for name, attr in var_dict.items():
        size_str = normal_size(attr[size_offset])
        print("| " + str(name) + " " * (name_len - len(str(name))), end="")
        print(" | " + str(attr[type_offset]) + " " * (type_len - len(str(attr[type_offset]))), end="")
        print(" | " + str(size_str) + " " * (size_len - len(size_str)), end="")
        print(" | " + str(attr[lock_offset]) + " " * (lock_len - len(str(attr[lock_offset]))) + " |")
    print("+-" + "-" * name_len + "-+-" + "-" * type_len + "-+-" + "-" * size_len + "-+-" + "-" * lock_len + "-+")


def lexical_analyzer(cmd):
    keywords = {"print", "remove", "rm", "rename", "copy", "clone", "exit", "quit"}
    token_specification = [
        ("number", r"\d+(\.\d*)?"),
        ("assign", r"="),
        ("name", r'[_A-Za-z][_A-Za-z0-9]*'),
        ("punctuation", r"\(\)\{\},"),
        ("skip", r"[ \t]+"),
        ("mismatch", r"."),
    ]
    token_regex = "|".join("(?P<%s>%s)" % pair for pair in token_specification)
    for m in re.finditer(token_regex, cmd):
        kind = m.lastgroup
        value = m.group(kind)
        if kind == "skip":
            pass
        elif kind == "mismatch":
            raise Exception("Unexpected token: %s" % value)
        elif:




if __name__ == "__main__":
    c = Client("219.223.243.8", 8088)
    while True:
        var = c.list()
        print_list(var)
        cmd = input(">>> ")
        tmp_list = cmd.split(" ")
        cmd_list = []
        for one_cmd in tmp_list:
            if len(one_cmd) != 0:
                cmd_list.append(one_cmd)
        if len(cmd_list) == 0:
            continue
        if cmd_list[0] == "print":
            if len(cmd_list) != 2:
                print("Usage: print <variable>")
                continue
            pprint.pprint(c.load(cmd_list[1]))
            print("")
        elif cmd_list[0] == "remove" or cmd_list[0] == "rm":
            if len(cmd_list) != 2:
                print("Usage: remove[rm] <variable>")
                continue
            print(c.remove(cmd_list[1]))
            print("")
        elif cmd_list[0] == "rename":
            if len(cmd_list) != 3:
                print("Usage: rename <old variable> <new variable>")
                continue
            print(c.rename(cmd_list[1], cmd_list[2]))
            print("")
        elif cmd_list[0] == "copy" or cmd_list[0] == "clone":
            if len(cmd_list) != 3:
                print("Usage: copy[clone] <src variable> <dst variable>")
                continue
            print(c.clone(cmd_list[1], cmd_list[2]))
        elif cmd_list[0] == "exit" or cmd_list[0] == "quit":
            if len(cmd_list) != 1:
                print("Usage: exit[quit]")
                continue
            c.close()
            break
        elif cmd_list[0] == "help" or cmd_list[0] == "?":
            if len(cmd_list) != 1:
                print("Usage: help[?]")
                continue
            print("print <variable>                          - print a variable.")
            print("remove[rm] <variable>                     - remove a variable.")
            print("rename <old variable> <new variable>      - rename a variable.")
            print("copy[clone] <src variable> <dst variable> - copy a variable to a new variable.")
            print("exit[quit]                                - quit management system.")
            print("help[?]                                   - print this message.")
            print("")
        else:
            print("Invild command: " + cmd)