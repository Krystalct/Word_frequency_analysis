# coding:utf8
# 去除目标文本停用词的模块

import pandas as pd
import os

from WordList import WordList

from count_times import RESULT_PATH as TARGET_FILE
from c_stopwords import RESULT_PATH as STOPW0RD_PATH

# 去掉停用词后的文件存储目录
NO_STOP_PATH = os.getcwd() + '/without_stopwords/'



def del_stopwords(target_file=TARGET_FILE, stopwords_path=STOPW0RD_PATH, store_path=NO_STOP_PATH):
    """
    从统计好词频的目标文件中删除停用词，并存储到store_path
    :param target_file: 统计好词频的目标文件
    :param stopwords_path: 停用词存储位置
    :param store_path: 删除停用词后的目标文件存放位置
    :return:
    """
    from ResultFile import ResultFile
    _rf_target = ResultFile(target_file)
    _rf_result = ResultFile(stopwords_path)

    for n in xrange(2, 7):
        stopwords_n = pd.read_csv(_rf_result.get(n), encoding='utf8')['word_segment']
        for items in stopwords_n:
            print items
        wl = WordList()
        wl.read_data(_rf_target.get(n))
        df_n = wl.get_data()
        df_n['is_stopword'] = df_n.index.isin(stopwords_n.tolist())
        df_n = df_n[df_n['is_stopword'] == False]
        del df_n['is_stopword']
        wl.set_data(df_n)
        wl.write_data(store_path +'/'+ wl.name + '.txt')


def main():
    del_stopwords()


if __name__ == '__main__':
    # del_stopwords(target_file, stopwords_path, store_path)
    from log_time import log_runtime

    log_runtime(main, "测试生成产生停用词的词频表")
