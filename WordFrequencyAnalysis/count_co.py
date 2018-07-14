# coding:utf8
"""计算词的凝固度和自由度模块"""
from WordList import WordList
from ResultFile import ResultFile
import os
CO_RESULT_PARTH = os.getcwd()+'/with_co/'


def split_word(word):
    '''
    将字符串 从所有可以切分的位置切成两半
    :param word:eg:ABC
    :return:list eg:返回切分后的字符串列表[[A,BC],[AB,C]]
    '''
    list_s = []
    # print len(word)
    for i in xrange(1, len(word)):
        word_left = word[0:i]
        word_right = word[i:]
        print "[%s,%s]" % (word_left, word_right)
        list_s.append([word_left, word_right])

    return list_s


def count_co(wordlist, result_path):
    """
    计算每个表中的词的凝固度
    :param wordlist: 一张词频表
    :param outputfile: 计算结果输出目录
    :return:
    """
    # 删除掉词频<=4的词不计算
    wordlist.d_times(4)
    df = wordlist.get_data()
    sum_times = df.times.sum()
    li_co = []
    for word in df.index:
        list_s = split_word(word)
        li_num = [float('inf'), float('inf')]
        for couple in list_s:
            df[u'a'] = df.index.str.startswith(couple[0])
            sum_a = df[df[u'a'] == True].times.sum()
            df[u'b'] = df.index.str.endswith(couple[1])
            sum_b = df[df[u'b'] == True].times.sum()
            del df[u'a'], df[u'b']
            if li_num[0] + li_num[1] > sum_a + sum_b:
                li_num = [sum_a, sum_b]
        sum_ab = df.at[word, u'times']
        co_word = float(sum_ab * sum_times) / (li_num[0] * li_num[1])
        print word,'的凝固度co=',co_word
        li_co.append(co_word)
        pass
    df[u'co'] = li_co
    wordlist.set_data(df)
    wordlist.write_data(result_path)


def count_co_word(word, wordlist):
    """计算词频表中某个单个词的凝固度"""

    df = wordlist.get_data()
    if word not in df.index:
        print("--------%s不在%s中--------") % (word, wordlist.name)
        raise ValueError()
    list_s = split_word(word)
    li_num = [float('inf'), float('inf')]
    for couple in list_s:
        df['a'] = df.index.str.startswith(couple[0])
        sum_a = df[df['a'] == True].times.sum()
        df['b'] = df.index.str.endswith(couple[1])
        sum_b = df[df['b'] == True].times.sum()
        del df['a'], df['b']
        if li_num[0] + li_num[1] > sum_a + sum_b:
            li_num = [sum_a, sum_b]
    sum_ab = df.at[word, 'times']
    sum_times = df.times.sum()
    co_word = float(sum_ab * sum_times) / (li_num[0] * li_num[1])

    print("\"%s\"的凝固度为：%.3f" % (word, co_word))
    return co_word
    pass


def count_co_all_test():
    from del_stopwords import NO_STOP_PATH
    inputfile = NO_STOP_PATH
    rfp = ResultFile(inputfile)
    for file in rfp.get_data().values():
        """遍历每个文件"""
        print file
        wl = WordList()
        wl.read_data(file)
        result_path = CO_RESULT_PARTH + wl.name + u'_co.txt'
        count_co(wl, result_path)

def count_co_all(input_path,result_path):
    """
    计算已经删除了停用词的所有词的凝固度并输出到文件
    :param input_path: 删除停用词的存储目录
    :param result_path: 带有凝固度值的词频表的存储位置
    :return:
    """
    rfp = ResultFile(input_path)
    for file in rfp.get_data().values():
        """遍历每个文件"""
        print file
        wl = WordList()
        wl.read_data(file)
        result_path = result_path + wl.name + u'_co.txt'
        count_co(wl, result_path)


if __name__ == '__main__':
    from log_time import log_runtime
    log_runtime(count_co_all_test, '统计红楼梦所有词凝固度')
