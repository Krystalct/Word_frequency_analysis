# -*- coding: utf-8 -*-：
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def plot_df(df, result_path):
    '''
    根据df画出其折线图并输出到文件
    :param df:pd.DataFrame(columns=[要画的词列表],index=回数）
    :return:
    '''

    fig, axes = plt.subplots(2, 2)
    ymax = np.max(df.values)  # 求词频最大的值
    yticks = np.arange(0,int(ymax // 10 + 2) * 10,10)
    # plt.figure(figsize=(10,60))
    print df
    df1 = df.loc[1:30]
    df2 = df.loc[31:60]
    df3 = df.loc[61:90]
    df4 = df.loc[91:120]
    df1.plot(kind='line', grid=True, ax=axes[0][0], yticks=yticks, xticks=[1, 10, 20, 30])
    df2.plot(kind='line', grid=True, ax=axes[0][1], yticks=yticks, xticks=[31, 40, 50, 60])
    df3.plot(kind='line', grid=True, ax=axes[1][0], yticks=yticks, xticks=[61, 70, 80, 90])
    df4.plot(kind='line', grid=True, ax=axes[1][1], yticks=yticks, xticks=[91, 100, 110, 120])

    # axes[0][0].set_title(u'词语词频变化图')
    # axes[0][0].set_xlabel(u'x:回数')
    # axes[0][0].set_ylabel(u'y:词频')

    # axes[0][1].set_title(u'词语词频变化图')
    # axes[0][1].set_xlabel(u'x:回数')
    # axes[0][1].set_ylabel(u'y:词频')

    # axes[1][0].set_title(u'词语词频变化图')
    # axes[1][0].set_xlabel(u'x:回数')
    # axes[1][0].set_ylabel(u'y:词频')

    # axes[1][1].set_title(u'词语词频变化图')
    # axes[1][1].set_xlabel(u'x:回数')
    axes[1][1].set_xlabel(u'x:回数  y:词频')

    plt.savefig(result_path, dpi=200)
    plt.show()

    pass


if __name__ == '__main__':
    data = pd.read_excel('/Users/krystal/Desktop/test.xlsx')
    plot_df(data)
