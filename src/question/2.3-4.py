# -*- coding:utf-8 -*-

"""
插入排序递归版本
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

# 插入操作
# 前的n-1个数组已经排序完成
def insert(A, n):
    i = n - 1
    temp = A[n]
    while i >= 0 and A[i] > temp:
        A[i + 1] = A[i]
        i -= 1
    A[i + 1] = temp
    return


def recursion_insert_sort(A, n):
    if n > 1:
        recursion_insert_sort(A, n - 1)
        insert(A, n)
        print A


if __name__ == '__main__':
    sort_list = []
    randoms(sort_list)
    print sort_list
    recursion_insert_sort(sort_list, len(sort_list) - 1)
    print sort_list
