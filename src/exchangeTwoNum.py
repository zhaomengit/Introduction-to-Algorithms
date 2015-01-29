# -*- coding:utf-8 -*-
# 交换两个变量的值的方法

if __name__ == "__main__":
    a = 3
    b = 6
    a ^= b
    b = a ^ b
    a ^= b
    print "a is %d" % a
    print "b is %d" % b
