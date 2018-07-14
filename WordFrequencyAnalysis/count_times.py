# -*- coding: utf-8 -*-：
"""
将文章分段统计词频并输出到文件
"""

import re
import pandas as pd
import zhon.hanzi
from log_time import log_runtime
from common import output_log
from file_func import *
from WordList import WordList

# 指定一次处理多少行
LINE_NUM = 2000
# 待处理的文件
TARGET_FILE_PATH = os.getcwd() + '/hlm.txt'
# 处理结果存放位置
RESULT_PATH = os.getcwd() + '/hlm_result/'


def filter_signs(s):
    """
    对表的每一行使用del_sign()
    并返回处理后的字符串
    :param s:pd.DataFrame()的一行，类型为Series
    :return:
    """

    def del_sign(str):
        '''
        删除字符串中除中文汉字以外的字符
        :param str: 字符串
        :return: 返回删除后的字符串
        '''
        # zhon.hanzi.characters是中文汉字（不包括中文标点符号）的集合
        str = re.findall('[%s]' % zhon.hanzi.characters, str)
        str = ''.join(str)
        return str

    return s.apply(del_sign)


class Segment():

    def __init__(self, input_file=TARGET_FILE_PATH, output_file=RESULT_PATH):
        """
        初始化Segment实例
        :param input_file: 待处理的文本文件
        :param ouput_file: 处理后的结果存储目录
        """
        self.__wBuffer = ''  # 存储分块处理时上一块余下的字符
        self.__df = pd.DataFrame()
        self.__n = 2
        self.__input_file = input_file
        self.__name = get_name(input_file)  # 根据输入的文件自动生成文件夹名作为segment的name属性值
        self.__storepath = {}  # 存储结果文件的存储目录
        result_path = mkfolder(output_file, self.__name)
        for i in xrange(2, 7):
            self.__storepath[i] = result_path + self.__name + '_' + str(i) + '.txt'
        print self.__storepath

    def count_times(self, n_word):
        """
        统计出字数为n_word的词并将结果存储到文件
        :param n_word:字数
        :return:
        """
        output_log('正在统计'+str(n_word)+'词词频，请稍后')
        chunks = pd.read_csv(self.__input_file,
                             header=None,
                             encoding='utf8',
                             chunksize=LINE_NUM,
                             dtype=str,
                             sep='\n',
                             names=[u'text_segment'])
        buffer = ''
        for chunk in chunks:
            self.__wBuffer = buffer
            self.__n = n_word
            self.__add(self.__work(chunk))
            buffer = self.__wBuffer
            pass
        # 将最后生成的词频表写入外存中
        wl = WordList()
        wl.set_data(self.__df)
        self.__df = pd.DataFrame()
        self.__wBuffer = ""
        wl.write_data(self.__storepath[n_word])

    def get_df(self):
        return self.__df

    def __add(self, df):
        """
        将另一个词频统计表加到缓存中
        :param df: 一个pd.DataFrame(columns=['word_segment','times'])
        :return:
        """
        self.__df = pd.concat([self.__df, df], axis=0)
        self.__df = self.__df.groupby(self.__df.index).sum()
        pass

    def __work(self, df):
        """
        处理一个df；将标点符号去掉然后用n字窗口切割再生成一个词频表
        :return:返回生成的词频表pd.DataFrame()
        """
        strsum = self.__pretreament(df)
        df = self.__nwindow(strsum)
        return df

    def count_all(self):
        for n in xrange(2, 7):
            self.count_times(n)
        pass

    def __pretreament(self, df):
        '''
        将读进来的df 先去除掉标点符号
        再加上上一块余下来的字符
        :return:
        '''
        df = df.apply(lambda x: filter_signs(x), axis=1)
        sumline = df.sum(axis=1)
        # out_list(sumline)
        str_temp = sumline.sum()
        # 加上上一个segment切分后余下的字符
        strsum = self.__wBuffer + str_temp
        return strsum

    def __nwindow(self, strsum):
        '''
        按n字的窗口 切分词
        将余下的不够n个字的存入self.__wBuffer
        :return:返回切得的词语列表pd.DataFrame
        '''
        # 计算字符串的长度-n  = strlen 为能切得的词的字数
        listr = []
        strlen = len(strsum) - self.__n + 1
        for i in xrange(0, strlen):
            strtemp = strsum[i:i + self.__n]  # 切片访问
            listr.append(strtemp)  # 将切得的词放入list
        self.__wBuffer = strsum[-(self.__n - 1):]
        # print ('余下的缓存字符：%s' % (self.__wBuffer))
        # 将list中的词放进DataFrame中 并统计词频
        df = pd.DataFrame({u'word_segment': listr})
        data = df.groupby(df.word_segment).size()
        # Optimizing Numeric Columns with Subtypes
        data = pd.to_numeric(data, downcast='unsigned')
        df = pd.DataFrame({'times': data})
        return df


def count_times(input_file=TARGET_FILE_PATH, output_file=RESULT_PATH):
    """
    测试统计词频的功能
    :return:
    """
    seg = Segment(input_file, output_file)
    seg.count_all()


def countall_test():
    log_runtime(count_times, u'测试统计所有字数词的词频，红楼梦，2000')


if __name__ == '__main__':
    """测试切一篇文章"""
    countall_test()
