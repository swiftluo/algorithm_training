# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# 斐波那契数列的应用

# -*- coding:utf\-8 -*-


class Solution:
    def jumpFloor(self, number):
        # write code here
        a = 1
        b = 1
        for i in range(number):
            a,b = b, a + b
        return a
