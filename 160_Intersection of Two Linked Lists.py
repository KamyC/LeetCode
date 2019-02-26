# Write a program to find the node at which the intersection of two singly linked lists begins.
#
# For example, the following two linked lists:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        set_A = set()
        curA = headA
        curB = headB
        while curA:
            set_A.add(curA)
            curA = curA.next
        while curB:
            if curB in set_A:
                return curB
            curB = curB.next