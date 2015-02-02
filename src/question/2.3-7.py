# coding:utf-8

"""
题目：描述一个运行时间为O(nlgn)算法
      给定n个整数集合S和另一个整数x,
      该算法能确定S中是存在两个和刚好为x的元素
"""

# 解题思路
# 1. 对S进行排序
# 2. 设置S' = {z : z = x − y for some y ∈ S}.
# 3. 对S'进行排序.
# 4. S和S'中如果有重复的，去掉重复的
# 5. 对S和S'进行合并.
# 6. 如果存在S中的两个元素和为x,那么在S和S'合并的集合中肯定有连续相同的值


# 例如 S = {a, b, c, d} (排序后)
# S' = {x-a, x -b, x -c , x-d} (排序后)
# 如果 a + c = x
# 那么 a = x - c
# S和S’合并之后a和x-c肯定是相邻相同的值