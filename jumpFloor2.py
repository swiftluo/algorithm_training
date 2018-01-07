# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

# -*- coding:utf-8 -*-


class Solution:
    def jumpFloorII(self, number):
        # write code here
        # fn = fn-1 + fn-2   + f1
        # fn-1 = fn-2   + f1
        # fn - fn-1 = fn-1
        # fn = 2fn-1
        if number == 1:
            return 1
        a = 1
        for i in range(number - 1):
            a = 2*a
        return a
