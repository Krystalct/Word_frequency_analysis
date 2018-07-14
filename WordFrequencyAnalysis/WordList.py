# -*- coding: utf-8 -*-：


import pandas as pd
from file_func import get_name


# xuci = ['而',
#         '何',
#         '乎',
#         '乃',
#         '其',
#         '且',
#         '然',
#         '若',
#         '所',
#         '为',
#         '焉',
#         '也',
#         '以',
#         '矣',
#         '于',
#         '之',
#         '则',
#         '者',
#         '与',
#         '因']


# def match_xuci(str):

#     '''
#     如果str中含有至少一个虚词，则返回True，否则返回False
#     :param str:
#     :return:
#     '''
#     pattern = ''.join(xuci)
#     # pattern=pattern.decode('utf8')
#     pat = u'[' + pattern + u']'
#     regex = re.compile(pat)
#     # print pat
#     mat = re.search(regex, str)
#     # print mat
#     if mat:
#         return True
#     return False


class WordList:
    __slots__ = ('__data', 'n')

    def __init__(self):
        self.__data = pd.DataFrame()
        self.name = ''
        self.n = 2
        pass

    def set_data(self, df):
        if not isinstance(df, pd.DataFrame):
            raise ValueError("传入的数据类型错误！")
        self.__data = df

    def get_data(self):
        return self.__data

    def read_data(self, filename):
        self.__data = pd.read_csv(filename, header=0, index_col=0, encoding='utf-8')
        self.name = get_name(filename)

    def write_data(self, filename):
        self.__data.to_csv(filename, header=True)

    def d_times(self, num):
        # 删掉词频小于num的词
        self.__data = self.__data[self.__data.times > num]

    def __add__(self, other):
        self.__data = self.__data.append(other.__data)


def test():
    input_file = u'/Users/krystal/Desktop/fr_result/hlm_2_fr.txt'
    output_file = u'/Users/krystal/Desktop/whatever.txt'
    other_file = u'/Users/krystal/Desktop/hlm_2_fr(all).txt'
    test = WordList()
    test.read_data(input_file)
    df = test.get_data()
    test1 = WordList()
    test1.read_data(other_file)
    df1 = test1.get_data()
    # df = test1.get_data().sort_values(by=['fr_left'],ascending=False).head(100)

    print test + test1

    # for item in sets:
    #     print item


if __name__ == '__main__':
    """管理生成的 词频表"""
    test()
