# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# 给出的所有元素都大于0，若数组大小为0，请返回0。

# -*- coding:utf-8 -*-
# 二分查找，直到找到相邻的两个数左边大于右边
# 也可以用min()函数直接求出数组最小值 


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        left = 0
        middle = -1
        right = len(rotateArray) - 1
        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:
                middle = right
                break
            middle = left + (right - left)/2
            if rotateArray[middle] >= rotateArray[left]:
                left = middle
            if rotateArray[middle] < rotateArray[left]:
                right = middle
        return rotateArray[middle]


