# coding:utf8
"""计算词的自由度模块"""
from WordList import WordList
import os

FR_RESULT_PARTH = os.getcwd() + '/fr_result/'


def c_information(num, sum):
    '''
     根据出现概率计算信息量
    :return:-(num/sum)*log((num/sum),2)
    '''
    p = float(num) / sum
    import math
    return -p * float(math.log(p, 2))


def count_fr(wordlist, wordlist_next, result_path=FR_RESULT_PARTH):
    # 只计算词频大于4的词的自由度
    wordlist.d_times(4)
    df = wordlist.get_data()
    del df[u'times']
    fr_left = []
    fr_right = []
    for word in df.index:
        left, right = _count_free(word, wordlist_next)
        fr_left.append(left)
        fr_right.append(right)
    df['fr_left'] = fr_left
    df['fr_right'] = fr_right
    wordlist.set_data(df)
    outfilename = result_path + '/' + wordlist.name + u'_fr.txt'
    wordlist.write_data(outfilename)
    pass


def _count_free(word_ab, wordlist):
    df = wordlist.get_data()
    fr_left = 0.0
    fr_right = 0.0
    df['a'] = df.index.str.startswith(word_ab)
    df_a = df[df['a'] == True]  # 构造word_ab的右邻字df
    df['b'] = df.index.str.endswith(word_ab)
    df_b = df[df['b'] == True]
    for word in df_a.index:
        fr_left = fr_left + c_information(df_a.at[word, 'times'], df_a.times.sum())
    for word in df_b.index:
        fr_right = fr_right + c_information(df_b.at[word, 'times'], df_b.times.sum())
    print '\"' + word_ab + '\"' + "的左自由度：" + str(fr_right)
    print '\"' + word_ab + '\"' + "的右自由度：" + str(fr_left)
    return fr_right, fr_left
    pass


def test():
    """
    根据去除停用词后的词频表，计算词的自由度
    并输出到文件
    :return:
    """
    from ResultFile import ResultFile
    from del_stopwords import NO_STOP_PATH
    inputfile = NO_STOP_PATH
    rfp = ResultFile(inputfile)
    for i in xrange(2, 3):
        f = rfp.get(i)
        f_next = rfp.get(i + 1)
        wl = WordList()
        wl.read_data(f)
        wl_next = WordList()
        wl_next.read_data(f_next)
        count_fr(wl, wl_next)


def count_fr_all(no_stop_words, result_path):
    """
    根据传入的去除停用词后的词计算词的自由度，并将结果输出到result_path
    :param no_stop_words: 去除停用词后的词频表
    :param result_path: 计算结果存储路径
    :return:
    """
    from ResultFile import ResultFile
    rfp = ResultFile(no_stop_words)
    for i in xrange(2, 5):
        f = rfp.get(i)
        f_next = rfp.get(i + 1)
        wl = WordList()
        wl.read_data(f)
        wl_next = WordList()
        wl_next.read_data(f_next)
        count_fr(wl, wl_next, result_path)


if __name__ == '__main__':
    from log_time import log_runtime
    log_runtime(test, u'计算  红楼梦 2词的自由度(取词频大于4的)')
