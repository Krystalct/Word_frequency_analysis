# -*- coding: utf-8 -*-：
import common
import os
common.chdefaultencoding()
'''
创建文件目录以及文件的功能模块
'''


# current_path = os.getcwd() + '/words_result'
def get_name(input_file):
    '''切分文件名'''
    import re
    li = re.split(u'/', input_file.encode('utf8'))
    name = re.split(u'\.', li[len(li) - 1])
    return name[0]


def set_curpath(filepath='/Users/krystal/Desktop/'):
    os.chdir(filepath)  # 更改当前工作路径
    # print os.getcwd()


def set_storepath(name=u'test'):
    '''用户输入文件存储路径，根据用户输入的name和文件路径创建一个文件夹'''
    storage_path = raw_input('输入文件存储路径:')
    print '您输入的文件存储路径为：' + storage_path

    if os.path.exists(storage_path):
        # 如果用户输入的文件存储路径存在
        # 则在用户输入路径下根据name值新建一个文件夹
        set_curpath(storage_path)
        mkfolder(os.getcwd(), name)


    else:
        print('文件路径\"' + storage_path + '\"不存在！请重新输入')
        set_storepath(name)


def mkfolder(path, name):
    """
    在指定路径str下创建一个文件夹
    :param str: 字符串存储文件路径
    :return:创建的文件夹地址

    """
    path = path + '/' + name + '_result/'
    isExists = os.path.exists(path)

    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print '-----文件目录' + path + ' 创建成功------'
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path + '已存在！-----\n重新输入一个文件夹路径'
        set_storepath(name)

    pass
    return path



def get_allfile(path):
    allfilelist = os.listdir(path)
    if allfilelist is None:
        print(path+"为空！")
    if '.DS_Store' in allfilelist:
        allfilelist.remove('.DS_Store')  # 删除macOs下目录配置文件
    for i in xrange(len(allfilelist)):
        allfilelist[i] = path + '/' + allfilelist[i]
    return allfilelist


if __name__ == '__main__':
    print get_name('/Users/krystal/Desktop/test_result/hlm.txt')
    set_storepath(u'你麻痹')
