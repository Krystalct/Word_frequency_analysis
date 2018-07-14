# -*- coding: utf-8 -*-：
import common
import pandas as pd
import re

common.chdefaultencoding()
import os

PLOT_LINE_PATH = os.getcwd() + '/'


class Chapter:
    def __init__(self, filename):
        '''
        读取一篇文章并将其按章节切分进行操作。

        '''
        self.__listr = []
        self.__pretreament(filename)
        pass

    def __pretreament(self, filename):
        """
        将文章读进内存并分回数
        :param filename:
        :return:
        """
        data = pd.read_csv(filename, encoding='utf8', header=None, names=[u'text_segment'])

        # from count_times import filter_signs
        from str_qtob import full_to_half
        data = data[u'text_segment'].apply(lambda x: full_to_half(x))
        str_sum = data.sum()
        patt = u'\s*第.{1,5}回\s+'
        self.__listr = re.split(patt, str_sum)
        del self.__listr[0]
        for item in self.__listr:
            print item
            print '\n'
        pass

    def get_listr(self):
        '''
        :return:
        '''
        return self.__listr
        pass

    def findallword(self, li_word, str):
        '''
        在str中找到所有词语列表中的词语
        :param li_word: 词语列表
        :param str: 字符串
        :return: 返回找到的所有词语的列表
        '''
        li_keyword = []
        for item in li_word:
            li_ci = re.findall(item, str)
            for word in li_ci:
                li_keyword.append(word)
            pass
        return li_keyword

    def main_work(self, li_word, pic_name):
        '''
        根据传入的词语列表，在每一章找到这些词语，然后统计词频，画出其折线图
        :param li_word:
        :return:
        '''
        data_sum = pd.DataFrame(columns=li_word)  # 新建一张表 作为画折线图的表存储相关内容
        s_data = pd.Series(dtype=int)

        for chapter in self.__listr:
            for word in li_word:
                word_times = len(re.findall(word, chapter))
                s_data[word] = word_times
                pass
            data_sum = data_sum.append(s_data, ignore_index=True)
        from plt_line import plot_df
        plot_df(data_sum, PLOT_LINE_PATH + pic_name)
        pass


def test():
    """输入要画的词频列表，输出折线图文件到result_path"""
    inputfile = '/Users/Krystal/Desktop/sanguo.txt'
    _myChapter = Chapter(inputfile)
    li_word = [u'曹操']
    _myChapter.main_work(li_word, '曹操.png')


if __name__ == '__main__':
    test()
