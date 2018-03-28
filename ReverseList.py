# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 先装到一个list里面再改变指针指向时间复杂度O(2*n^2)
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        l = []
        while pHead:
            l.append(pHead)
            pHead = pHead.next
        for i in range(0, len(l)):
            if i == 0:
                l[0].next = None
            else:
                l[i].next = l[i-1]
        return l[-1]


# 直接改变指针指向 时间复杂度O(n^2)
class Solution2:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead

        last = None

        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last

