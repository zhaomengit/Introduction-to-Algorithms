# -*- coding:utf-8 -*-
"""
查找最大子序列时间复杂度为O(n)的算法
"""


class MaxSubarray:

    def __init__(self):
        self.left = 0    # 左边的坐标
        self.right = 0    # 右边的坐标
        self.sum_sub = 0  # 最大子数组的和


def find_maximum_subarray(A, low, high):
    list_max_subarry = [MaxSubarray() for i in xrange(0, high - low)]
    list_max_subarry[0].left = low
    list_max_subarry[0].right = low + 1
    list_max_subarry[0].sum_sub = A[low]

    for i in xrange(low + 1, high):
        if list_max_subarry[i - 1].sum_sub < 0:
            list_max_subarry[i].left    = i
            list_max_subarry[i].right   = i + 1
            list_max_subarry[i].sum_sub = A[i]
            print list_max_subarry
        else:
            list_max_subarry[i].left = list_max_subarry[i - 1].left
            list_max_subarry[i].right = i + 1
            list_max_subarry[i].sum_sub = list_max_subarry[i - 1].sum_sub + A[i]

    max_l = list_max_subarry[0]
    for k in xrange(low + 1, high):
        print k
        if max_l.sum_sub < list_max_subarry[k].sum_sub:
            max_l = list_max_subarry[k]

    return max_l

if __name__ == '__main__':
    list_test = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    sub = find_maximum_subarray(list_test, 0, len(list_test))
    print "the low is %d, the right is %d, the list_test is %d" % (sub.left, sub.right, sub.sum_sub)