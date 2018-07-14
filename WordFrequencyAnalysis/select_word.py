# coding:utf8
"""
根据已经生成的withco（pd.DataFrame(columns=['times','co'],index=['word_segment']）
和已经生成的fr_result(pd.DataFrame(columns=['fr_left','fr_right'],index=['word_segment'])
中的co和fr_left,fr_right字段筛选词，筛选词的标准为stand=co*(fr_left*fr_right)
"""
from WordList import WordList
import pandas as pd
import os
from count_co import CO_RESULT_PARTH
from count_fr import FR_RESULT_PARTH
SELECT_RESULT_PATH = os.getcwd()+'/selected_result/'


def _count_s(x):
    score = x['co'] * (x['fr_left'] * x['fr_right'])
    return score
    pass


def select_word(df_co, df_fr, result_path, score_stand=100.0, co_stand=10.0, fr_stand=0.3):
    """
    计算每个词的score值并存储到文件result_path
    :param df_co:pd.DataFrame(columns=['times','co'],index.name='word_segment')
    :param df_fr:pd.DataFrame(columns=['fr_left','fr_right'],index.name='word_segment')
    :param result_path:存放score计算结果文件的路径
    :param score_stand:保留的词的score 的最低值
    :param co_stand:保留的词的co的最低值
    :param fr_stand:保留的词的fr的最低值
    :return:
    """
    # 先删除fr值小于10的
    df_fr = df_fr[(df_fr['fr_left'] > fr_stand) &
                  (df_fr['fr_right'] > fr_stand)]
    # 再删除co值小于co_stand=0.3的
    df_co = df_co[(df_co['co'] > co_stand)]
    # 将两张表合并
    df = pd.merge(df_co, df_fr, right_index=True, left_index=True)
    # print df
    # 计算score
    df['score'] = df.apply(lambda x: _count_s(x), axis=1)
    # df.columns=['times','fr_left','fr_right','score']
    df = df.sort_values(by=['score'], ascending=False)
    df = df[df['score'] > score_stand]
    _wordlist = WordList()
    _wordlist.set_data(df)
    _wordlist.write_data(result_path)



def test_select_word():
    '''测试4字词的score值计算'''
    input_co = u'/Users/Krystal/Desktop/with_co/hlm_4_co.txt'
    input_fr = u'/Users/Krystal/Desktop/hlm_4_fr.txt'
    _wl_co = WordList()
    _wl_fr = WordList()
    _wl_co.read_data(input_co)
    _wl_fr.read_data(input_fr)
    result_path = SELECT_RESULT_PATH + _wl_co.name[0:len(_wl_co.name) - 2] + 'score.txt'
    select_word(_wl_co.get_data(), _wl_fr.get_data(), result_path)
    pass

def select_word_all(co_result=CO_RESULT_PARTH,fr_result=FR_RESULT_PARTH,
                    result_path=SELECT_RESULT_PATH,score=100.0,co=0.3,fr=1.5):
    """
    根据已经计算出的凝固度和自由度计算score
    并根据score，co，fr筛选计算结果
    将筛选后的计算结果输出到文件
    :param co_result: 凝固度计算结果存储路径
    :param fr_result: 自由度计算结果存储路径
    :param result_path:筛选结果的存储路径
    :param score: 用来筛选词的score标准值
    :param co: 用来筛选词的co的标准值
    :param fr: 用来筛选词的fr 的标准值
    :return:
    """
    from ResultFile import ResultFile
    _rsf_co = ResultFile(co_result)
    _rsf_fr = ResultFile(fr_result)
    for i in xrange(2, 6):
        _wl = WordList()
        _wl.read_data(_rsf_co.get(i))
        df_co = _wl.get_data()
        _wl.read_data(_rsf_fr.get(i))
        df_fr = _wl.get_data()
        output_path = result_path +'/'+ _wl.name[0:len(_wl.name) - 2] + 'score.txt'
        select_word(df_co, df_fr, output_path,score,co,fr)
    pass
if __name__ == '__main__':
    from log_time import log_runtime
    log_runtime(select_word_all, '测试，通过计算score选择词')
