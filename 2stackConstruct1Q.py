# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
# -*- coding:utf-8 -*-

# 不是线程安全的，多线程要加锁
class Solution:
    stack_push = []
    stack_pop = []
        
    def push(self, node):
        # write code here
        self.stack_push.append(node)
        
    def pop(self):
        while len(self.stack_push) != 0:
            self.stack_pop.append(self.stack_push.pop())
        result = self.stack_pop.pop()
        while len(self.stack_pop) != 0:
            self.stack_push.append(self.stack_pop.pop())
        return result
