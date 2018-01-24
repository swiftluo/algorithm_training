# -*- coding:utf-8 -*-

# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。32位机器


class Solution:
    def number_of_1(self, n):
        # write code here
        return sum([(n >> i & 1) for i in range(0, 32)])
