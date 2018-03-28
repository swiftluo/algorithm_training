# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 解法一 先将单链表正序装到数组中，在取倒数第k个元素


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        l = []
        while not head:
            l.append(head)
            head = head.next
        if k > len(l) or k < 1:
            return
        return l[-k]


# 解法二 移动pre和last两个指针并记录pre和last的间隔index


class Solution2:
    def FindKthToTail(self, head, k):
        # write code here
        if not head:
            return head
        if k == 0:
            return None
        pre = head
        last = head
        index = 1
        while last.next:
            last = last.next
            index += 1
            if index > k:
                pre = pre.next
        if index < k:
            return None
        return pre


