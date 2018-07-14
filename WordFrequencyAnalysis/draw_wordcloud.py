# -*- coding: utf-8 -*-：
import pandas as pd
from WordList import WordList
import os

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import ImageColorGenerator

#绘制的词云的输出文件
RESULT_PIC =os.getcwd()+'/test.png'


def painting(df, result_path, mask_pic_path=os.getcwd() + '/alice.png'):
    '''
    根据df中的词频信息    画成词云 输出到目标路径（result_path）
    :param df:pd.DataFrame()
    :param result_path:输出路径
    :param mask_pic_path:作为mask的图片路径
    :return:
    '''
    # 检查传入的df是否有词频信息
    if isinstance(df, pd.DataFrame):
        if 'times' not in df.columns:
            raise ValueError
        # df = df.sort_values(by=['times'], ascending=False)
        df = df['times']

    w_dict = df.to_dict()
    image = Image.open(mask_pic_path)
    graph = np.array(image)
    image_color = ImageColorGenerator(graph)
    wc = WordCloud(mask=graph,
                   # max_font_size=40,
                   random_state=86,
                   # max_words=1000,
                   # relative_scaling=0,
                   color_func=image_color,  # 字体颜色为背景图片的颜色
                   scale=5,
                   background_color='white',
                   font_path='/Library/Fonts/Arial Unicode.ttf',
                   prefer_horizontal=1).fit_words(w_dict)
    # 显示词云图
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    wc.to_file(result_path)


def plt_n_word(sourcefile,result_path, mask_pic=os.getcwd() + '/alice.png', **kwargs):
    """
    画出经过选择的词的词云图(经过选择的词存在SELECT_RESULT_PATH)
    :param sourcefile:经过选择的词频统计文件
    :param result_path: 绘制的词云输出文件
    :param mask_pic: 画词云的mask
    :param **kwargs: 用来传递参数 n=num，传入后，只画n字词的词云
    :return:
    """
    from ResultFile import ResultFile
    rsf = ResultFile(sourcefile)
    print(rsf.get_data())
    # 如果传入关键字参数n=num，则只绘制n字词的词云
    if len(kwargs) == 1:
        num = kwargs.pop('n')
        _wl = WordList()
        _wl.read_data(rsf.get(num))
        df = _wl.get_data()
    else:
        # 否则就绘制全部字数词的词云
        _wl = WordList()
        _wl.read_data(rsf.get(2))
        for i in xrange(3, 6):
            _wl_next = WordList()
            _wl_next.read_data(rsf.get(i))
            _wl + _wl_next
            pass

        df = _wl.get_data()

    print df
    painting(df, result_path, mask_pic)


def test_plt():
    """测试绘制所有字数的词的词云"""
    from select_word import SELECT_RESULT_PATH
    plt_n_word(SELECT_RESULT_PATH,'/Users/Krystal/Desktop/选择后的所有词.png')
    # 测试绘制 5字词词云
    # plt_n_word(RESULT_PIC, n=5)
    pass

if __name__ == '__main__':
    test_plt()
