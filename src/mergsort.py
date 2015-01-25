# -*- coding:utf-8 -*-

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

def merge(A, p, q, r):
    """
    功能:
    A数组中A[p]-A[q]，A[q+1]- A[r]已经排好序了，
    把两段序列合并成一个，使A[p]-A[r]序列排好
    :param A:数组A
    :param p:最左端序列
    :param q:中间序列
    :param r:最后端的序列
    :return:
    """

    # 确定前一段序列的长度
    n1 = q - p + 1
    n2 = r - q
    left = A[p:q + 1]     # 注意python切片操作不包括右面的值
    right = A[q + 1:r + 1]
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            A[k] = left[i]
            k += 1
            i += 1
        else:
            A[k] = right[j]
            k += 1
            j += 1

    while i < n1:
        A[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = right[j]
        j += 1
        k += 1

    return


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) / 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

if __name__ == "__main__":
    s_list = []
    randoms(s_list)
    print s_list
    merge_sort(s_list, 0, len(s_list) - 1)
    print s_list
