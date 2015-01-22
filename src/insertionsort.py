# -*- coding:utf-8 -*-
from random import randint

def randoms(n):
    """
    产生10随机数
    """
    for i in xrange(0, 50):
        x = randint(0, 500)
        n.append(x)
    return


def insertion_sort(sort_arr):
    for j in xrange(1, len(sort_arr)):
        key = sort_arr[j]
        i = j - 1
        while i >= 0 and key < sort_arr[i]:
            sort_arr[i + 1] = sort_arr[i]
            i -= 1
        sort_arr[i + 1] = key
    return


if __name__ == '__main__':
    arr = []
    randoms(arr)
    print "begin sort:"
    print arr
    insertion_sort(arr)
    print "after sort:"
    print arr