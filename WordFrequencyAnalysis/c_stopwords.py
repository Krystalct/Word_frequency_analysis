# coding:utf8
"""计算停用词的模块"""
import os
import pandas as pd
from file_func import get_allfile, mkfolder, get_name
from log_time import log_runtime
import WordList
from common import output_log
STOP_SOURCE = os.getcwd() + '/stopword_source/'
RESULT_PATH = os.getcwd() + '/stopwords/'

STOP_RESULT = os.getcwd() + '/stopwords_result/'


def __getallfile(path):
    """
    获取统计词频后的产生停用词的文件列表并返回
    :param path:
    :return:dict{sanguo_result:pd.Serires({2:sanguo_2.txt,3:sanguo_3.txt,...}),
    shuihu_result:pd.Series(),..}
    """
    dict_path = {}
    allfilelist = os.listdir(path)
    if '.DS_Store' in allfilelist:
        allfilelist.remove('.DS_Store')  # 删除macOs下目录配置文件
    for file in allfilelist:
        # print file
        filepath = os.path.join(path, file)
        if not os.path.exists(filepath):
            raise OSError()
        subfiles = os.listdir(filepath)
        if '.DS_Store' in subfiles:
            subfiles.remove('.DS_Store')  # 删除macOs下目录配置文件
        li = []
        for items in subfiles:
            li.append(int(items[-5:-4]))
        series_temp = pd.Series(subfiles, index=li)
        dict_path[filepath] = series_temp
    return dict_path


def c_stopword_result(stopword_source=STOP_SOURCE, result_path=STOP_RESULT):
    """统计最终会产生停用词的文本文件，将词频统计结果存储到STOP_RESULT中"""
    sourcefiles = get_allfile(stopword_source)
    # 遍历文件夹下的子目录 分别统计词频
    for file in sourcefiles:
        from count_times import Segment
        seg = Segment(file, result_path)
        output_log('开始统计'+get_name(file)+'的词频')
        seg.count_all()
    pass


def c_stopwords_all(inputpath=STOP_RESULT, output_path=RESULT_PATH):
    """从stopword_result中读取统计词频后的文件，取共同词生成停用词"""
    dictpath = __getallfile(inputpath)
    for i in xrange(2, 7):
        _c_stopwords(i, dictpath, output_path)


def _c_stopwords(n, dict_path, output_path):
    """
    找出字数为n的词的共同词作为停用词并输出到output_path
    :param n:字数
    :param dict_path:源文件目录
    :param output_path:结果文件目录
    :return:
    """
    wl = WordList.WordList()

    keys = dict_path.keys()
    dic1 = dict_path[keys[0]]
    wl.read_data(keys[0] + '/' + dic1[n])

    for i in keys[1:]:
        path = i + '/' + dict_path[i][n]
        print path
        wl = WordList.WordList()
        wl.read_data(path)
        words = wl.get_data().index.intersection(wl.get_data().index)
    df = pd.DataFrame({'word_segment': list(words)})
    output_file = output_path + '/stopwords_' + str(n) + '.txt'
    df.to_csv(output_file, index=False)
    print df


def test_cstopwords():
    """测试统计所有字数的停用词"""

    c_stopword_result()  # 统计停用词源文件词频
    c_stopwords_all()  # 根据统计结果产生停用词
    pass


if __name__ == '__main__':
    log_runtime(test_cstopwords, "测试，统计三国和水浒的词频")
