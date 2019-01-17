# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        adder_1 = 0
        adder_2 = 0
        flag_1 = 0
        flag_2 = 0
        while (l1):
            adder_1 += l1.val * 10 ** flag_1
            flag_1 += 1
            l1 = l1.next

        while (l2):
            adder_2 += l2.val * 10 ** flag_2
            flag_2 += 1
            l2 = l2.next
        res = adder_1 + adder_2
        fin = []
        str_res = str(res)
        length = len(str_res)
        for i in range(length):
            temp = int(str_res[i])
            fin.append(temp)
        fin.reverse()
        return fin