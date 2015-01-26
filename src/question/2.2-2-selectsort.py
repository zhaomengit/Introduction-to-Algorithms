# -*- coding:utf-8 -*-

"""
插入排序的代码
"""


from random import  randint

random_num = 10      # 随机数的个数
random_scope = 400   # 随机数的范围


def randoms(arg_arr):
    """
    产生50随机数
    """
    for i in xrange(0, random_num):
        x = randint(0, random_scope)
        arg_arr.append(x)
    return


def select_sort(arg_arr):
    """
    选择排序
    """
    for i in xrange(0, len(arg_arr) - 1):
        small = i
        for j in xrange(i + 1, len(arg_arr)):
            if arg_arr[small] > arg_arr[j]:
                small = j
        temp = arg_arr[i]
        arg_arr[i] = arg_arr[small]
        arg_arr[small] = temp
    return

if __name__ == '__main__':
    arr = []
    randoms(arr)
    print "begin sort:"
    print arr

    select_sort(arr)

    print "after sort:"
    print arr
