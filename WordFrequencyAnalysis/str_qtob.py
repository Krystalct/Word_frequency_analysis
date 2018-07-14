# -*- coding: utf-8 -*-：
"""
分章回时 写的正则表达式 发现全角空格不能匹配\s
将全角字符转为半角字符，便于统一处理
"""


def full_to_half(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
            inside_code -= 65248

        rstring += unichr(inside_code)
    return rstring


def test():
    """测试full_to_half()全角转半角功能"""
    print ord(full_to_half(u'\u3000'))
if __name__ == '__main__':
    test()