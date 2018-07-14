# -*- coding: utf-8 -*-：
from count_times import count_times
import os
import re
from common import output_log
import sys

TARGET_RESULT = '/Users/Krystal/Desktop/hlm_result'
STOPWORD_PATH = ''


def input_file_path():
    """
        输入已经存在的文件路径并返回该路径
    :return:
    """
    path = str(raw_input('请输入文件路径，以换行符结束:'))
    if os.path.isfile(path):
        if path.endswith('.txt') or path.endswith('.png'):
            print '输入路径为：', path
            return path

    output_log('输入文件路径错误或者该文件不存在')
    print('按1重新输入或其他任意键结束')
    choose = int(raw_input())
    if choose == 1:
        return input_file_path()
    else:
        sys.exit()
    pass


def input_directory():
    """
    输入文件目录路径并返回该路径
    :return:
    """
    print '请输入文件目录，以换行符结束:'
    path = str(raw_input())
    if os.path.isdir(path):
        print '输入目录为：', path
        return path
    output_log('输入文件目录路径错误或者该目录不存在')
    print('按1重新输入或其他任意键结束')
    choose = int(raw_input())
    if choose == 1:
        return input_directory()
    else:
        sys.exit()
    pass


def c_times_user():
    """
    统计目标源文件词频，存储到外存，并返回结果路径
    :return:
    """
    output_log('输入要统计词频的文本文件')
    input_file = input_file_path()
    output_log('输入结果文件存放位置')
    output_file = input_directory()
    output_log('开始统计词频')
    count_times(input_file, output_file)
    output_log('词频统计完毕！')
    global TARGET_RESULT
    TARGET_RESULT = output_file
    return output_file
    pass


def d_stopwords_user():
    """
    在统计完目标源文件词频的基础上
    产生停用词
    :return:
    """
    from c_stopwords import c_stopword_result, c_stopwords_all
    from del_stopwords import del_stopwords
    output_log('请输入产生停用词的源文件路径')
    input_file = input_directory()
    output_log('请输入停用词源文件词频统计的结果存放路径')
    output_file = input_directory()
    output_log('开始统计停用词源文件词频信息')
    c_stopword_result(input_file, output_file)
    output_log('停用词源文件词频统计完毕')
    output_log('请输入停用词存放路径')
    stopwords_result = input_directory()
    c_stopwords_all(output_file, stopwords_result)
    output_log('停用词统计完毕')
    output_log('输入删除停用词后的结果存储路径')
    result_path = input_directory()
    del_stopwords(TARGET_RESULT, stopwords_result, result_path)

    global STOPWORD_PATH
    STOPWORD_PATH = result_path
    return result_path


def input_pic_name():
    """
    输入图片存储路径并检查该路径是否合法
    :return:
    """
    path = raw_input()
    if os.path.isdir(os.path.dirname(path)):
        if path.endswith('.png') or path.endswith('.jpg'):
            return path
    output_log('输入文件路径错误或者该路径不存在')
    print('按1重新输入或其他任意键结束')
    choose = int(raw_input())
    if choose == 1:
        return input_pic_name()
    else:
        sys.exit()
    pass


def input_stand():
    """
    选择是否输入选择词的参数
    输入参数co，fr，score
    :return:
    """
    output_log('是否输入选择词的参数?\n1.是\n2.否（采用默认值co=2.0,fr=1.0,score=100.0）\n')

    choose = int(raw_input('输入1或2:'))
    if choose == 2:
        output_log('开始计算')
    else:
        if choose == 1:
            output_log('输入参数co:')
            co = float(raw_input())
            output_log('输入的co值为：' + str(co))
            output_log('输入参数fr:')
            fr = float(raw_input())
            output_log('输入的fr值为：' + str(fr))
            output_log('输入参数score:')
            score = float(raw_input())
            output_log('输入的co值为：' + str(score))
            output_log('开始计算')
            return co, fr, score
    return 10.0, 0.3, 100.0


def select_word_user():
    """
    用户输入+筛选词语后词云输出
    :return:
    """
    # 计算凝固度
    from count_co import count_co_all
    output_log('请输入已经删除停用词的词频表目录')
    input_path = input_directory()
    output_log('请输入凝固度co的计算结果存储目录')
    co_result_path = input_directory()
    output_log('开始计算凝固度')
    count_co_all(input_path, co_result_path)
    output_log('凝固度计算完毕')
    # 计算自由度
    output_log('请输入自由度fr的计算结果存储目录')
    fr_result_path = input_directory()
    from count_fr import count_fr_all
    count_fr_all(input_path, fr_result_path)
    output_log('自由度计算完毕')
    # 筛选词语
    # co_result_path = '/Users/Krystal/Desktop/with_co'
    # fr_result_path = '/Users/Krystal/Desktop/fr_result'
    from select_word import select_word_all
    output_log('请输入筛选结果的存储路径')
    selected_word_path = input_directory()
    # selected_word_path = '/Users/Krystal/Desktop/test'
    # 输入筛选词的标准
    co, fr, score = input_stand()
    select_word_all(co_result_path, fr_result_path, selected_word_path, co=co, fr=fr, score=score)
    from draw_wordcloud import plt_n_word
    output_log('请输入绘制的词云存储路径')
    pic_path = input_pic_name()
    plt_n_word(selected_word_path, pic_path)

    pass


def draw_line_user():
    """
    用户输入待处理的源文件存储路径和要绘制成折线图的词
    绘制折现图并输出到文件
    :return:
    """
    from chapters_line import Chapter
    output_log('输入待处理的源文件路径：')

    input_file = input_file_path()
    _chpater = Chapter(input_file)
    output_log('输入待绘制的词：（以逗号隔开）')
    word_str = raw_input()
    word_list = word_str.split(',')
    for i in xrange(0,len(word_list)):
        word_list[i] = word_list[i].decode('utf8')
    _chpater.main_work(word_list, 'test')

    pass


def draw_wc_user():
    """
    用户输入要统计词频的源文件，
    要产生停用词的源文件，各种中间存储路径
    画出词云输出到文件
    """
    c_times_user()
    d_stopwords_user()
    select_word_user()
    pass


if __name__ == '__main__':
    draw_wc_user()

    # draw_line_user()
