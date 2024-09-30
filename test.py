# -*- coding: utf-8 -*-
# @Time  : 2024/9/30 14:30
# @Author: game4d@163.com
from pycolors_kit import ColorEx


def test():

    color = ColorEx()

    print(color.get_name_by_hex('#fe9956'))
    print(color.get_color_by_name('acapulco sun'))


if __name__ == '__main__':
    test()