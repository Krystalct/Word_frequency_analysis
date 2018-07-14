# -*- coding: utf-8 -*-：
import pandas as pd


def mem_usage(pandas_obj):
    if isinstance(pandas_obj, pd.DataFrame):
        usage_b = pandas_obj.memory_usage(deep=True).sum()  # 单位 byte
    else:  # we assume if not a df it's a series
        usage_b = pandas_obj.memory_usage(deep=True)
    if usage_b > 1024:
        usage_mb = float(usage_b) / 1024 ** 2  # convert bytes to megabytes
        return "{:.4f} MB".format(usage_mb)
    return "{:}B".format(usage_b)


if __name__ == '__main__':
    pass