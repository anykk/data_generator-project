from os import listdir
from os.path import isdir
from os.path import isfile
import json
import pprint


def func():
    dirs = []
    for file in listdir():
        if isdir(file) and '_' not in file:
            dirs.append(file)
    return dirs


if __name__ == "__main__":
    print(func())
    en = __import__(func()[0])
    pprint.pprint(locals())


