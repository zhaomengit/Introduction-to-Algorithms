# coding:utf-8
"""
二分查找递归和非递归
"""

from random import randint

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


def binary_find(A, low, high, element):
    while low <= high:
        mid = (low + high) / 2
        if A[mid] == element:
            return mid
        elif A[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def recursion_binary_find(A, low, high, element):
    if low > high:
        return -1
    mid = (low + high) / 2
    if A[mid] == element:
        return mid
    elif A[mid] > element:
        return recursion_binary_find(A, low, mid - 1, element)
    else:
        return recursion_binary_find(A, mid + 1, high, element)


if __name__ == '__main__':
    f_list = []
    randoms(f_list)
    f_list.sort()
    print f_list
    ele = raw_input("find element > ")                      # 通过raw_input获取输入的是字符串，下面需要使用int来转换
    # index = binary_find(f_list, 0, len(f_list) - 1, int(element))
    index = recursion_binary_find(f_list, 0, len(f_list) - 1, int(ele))
    print index
