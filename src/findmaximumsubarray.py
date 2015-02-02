# -*- coding:utf-8 -*-

import sys
"""
求最大子数组递归算法
"""


def find_max_crossing_subarray(array, low, mid, high):
    left_sum = -sys.maxint - 1    # 最小的整数
    sum_num = 0
    for i in xrange(mid, low - 1, -1):
        sum_num += array[i]
        if sum_num > left_sum:
            left_sum = sum_num
            max_left = i

    right_sum = -sys.maxint - 1
    sum_num = 0
    for i in xrange(mid + 1, high + 1):
        sum_num += array[i]
        if sum_num > right_sum:
            right_sum = sum_num
            max_right = i
    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(array, low, high):
    if low == high:                     # 只有一个元素的时候
        return low, high, array[low]
    else:
        mid = (low + high) / 2
        left_low, left_high, left_sum = find_maximum_subarray(array, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(array, mid + 1, high)
        crossing_low, crossing_high, crossing_sum = find_max_crossing_subarray(array, low, mid, high)

        if left_sum >= right_sum and left_sum >= crossing_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= crossing_sum:
            return right_low, right_high, right_sum
        else:
            return crossing_low, crossing_high, crossing_sum


if __name__ == '__main__':
    list_test = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    low_a, right_a, sum_a = find_maximum_subarray(list_test, 0, len(list_test) - 1)
    print "the low is %d, the right is %d, the list_test is %d" % (low_a, right_a, sum_a)
