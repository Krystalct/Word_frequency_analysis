# coding:utf8
import datetime

import pandas as pd
import common
import os

path = os.getcwd() + u'/MyLog/recordtime.csv'


def log_runtime(func, info):
    df = pd.DataFrame(columns=[u'info', u'spend_time'])
    starttime = datetime.datetime.now()
    # long running
    func()
    endtime = datetime.datetime.now()
    spend_time = (endtime - starttime)
    current_time = datetime.datetime.now()
    df.loc[current_time] = [info, spend_time]
    df.to_csv(path, mode='a+',header=False)


def func():
    sum = 0
    for i in xrange(1, 101):
        sum = sum + i + sum * i


if __name__ == '__main__':
    log_runtime(func, 'wo')
