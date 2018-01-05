# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
# n<=39
# -*- coding:utf-8 -*-
# 非递归实现，递归会导致栈溢出，编译器有对尾递归优化的可以使用尾递归实现


class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n >= 3:
            s = []*n
            s.append(1)
            s.append(1)
            for i in xrange(2,n):
                s.append(s[i-1]+s[i-2])
            return s[n-1]
