# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
# -*- coding:utf-8 -*-
# 核心思想是倒推铺完2*n之前的一步是什么状态，只能两种情况，横着一条，两条竖着的。得出递推公式fn = fn-1 + fn-2

class Solution:
    def rectCover(self, number):
        # write code here
        # f1 = 1 f2 = 2 f3 = 3 f4 = 5
        # fn = fn-1 + fn-2
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        a = 1
        b = 1
        for i in range(number-1):
            a,b = b,a + b
        return b
