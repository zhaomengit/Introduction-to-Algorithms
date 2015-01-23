# -*- coding:utf-8 -*-
"""
2-1-4:
把两个二进制整数加起来
这两个整数分别存储在两个n元组A和B中
这两个整数的和应该按二进制形式存储在一个（n+1）元组C中
"""
from random import randint

# ab有5位
index = 5


def randoms_to_list(arg_list):
    for i in xrange(0, index):
        arg_list[i] = randint(0, 1)
    return


def add_binary_num(a, b, c):
    for i in xrange(0, len(a)):
        temp = a[i] + b[i]
        c[i] += temp
        c[i + 1] += c[i] / 2
        c[i] %= 2

    return

if __name__ == '__main__':
    first_num = [0] * index
    second_num = [0] * index
    sum_num = [0] * (len(first_num) + 1)
    randoms_to_list(first_num)
    randoms_to_list(second_num)
    add_binary_num(first_num, second_num, sum_num)

    first_num.reverse()
    second_num.reverse()
    sum_num.reverse()

    print "the first num is :"
    print first_num

    print "the second num is :"
    print second_num

    print "the sum is:"
    print sum_num
