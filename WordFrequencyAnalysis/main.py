# -*- coding: utf-8 -*-：


def main():
    import word_analysis_func
    word_analysis_func.output_log('请选择：\n\n1.统计词频绘制词云图\n\n2.统计词频绘制折线图\n\n3.退出')
    try:
        choose = int(raw_input())
    except ValueError:
        print('输入不合法！请重新输入')
        return main()
        pass
    if choose == 1 or choose==2:
        if choose == 2:
            print'即将开始统计词频绘制词云!'
            word_analysis_func.draw_line_user()
        else:
            print'即将开始统计词频绘制折线图!'
            word_analysis_func.main()

    else:
        if choose == 3:
            print'------退出------'
            import sys
            sys.exit()
        else:
            print('输入不合法！请重新输入')
            return main()
    pass


if __name__ == '__main__':
    main()
