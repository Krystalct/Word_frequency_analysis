# -*- coding: utf-8 -*-：
def chdefaultencoding():
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')  # 改变默认编码模式
    print "更改编码为：" + sys.getdefaultencoding()


def output_log(op_str):
    print  '======================================', '\n'
    print op_str
    print '======================================'


if __name__ == '__main__':
    from WordList import WordList

    wl = WordList()
    wl.read_data(u'/Users/Krystal/Desktop/hlm_2_fr.txt')
    df = wl.get_data()
    df = df[df['fr_left'] > 1]
    df = df[df['fr_right'] > 1]
    wl.set_data(df)
    wl.write_data(u'/Users/Krystal/Desktop/hlm_review.txt')
