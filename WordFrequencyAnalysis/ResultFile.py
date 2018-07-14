# -*- coding: utf-8 -*-
import common
import os
import pandas as pd
from file_func import get_allfile,get_name

common.chdefaultencoding()


def get_index(filename):
    # 取文件名的倒数第五位作为索引用
    from re import findall
    return int(findall('\d', get_name(filename))[0])
    pass


class ResultFile:
    "获取某个文件目录下的所有文件生成一个字数n和文件名对应的Series,便于索引"

    # 目标文件名为..\xxx_1.txt
    def __init__(self, path):
        self.__data = {}
        for file in get_allfile(path):
            n = get_index(file)
            self.__data[n] = file

    def get_data(self):
        return self.__data

    def get(self, n):
        return self.__data[n]


if __name__ == '__main__':
    rsf = ResultFile(u"/Users/krystal/Desktop/withoutStopwords/")
    print rsf.get_data()
    keys = rsf.get_data().keys()
    print(keys)
