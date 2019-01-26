# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l_1 = []
        l_2 = []
        fin = []
        while (l1):
            l_1.append(l1.val)
            l1 = l1.next
        while (l2):
            l_2.append(l2.val)
            l2 = l2.next
        fin = l_1 + l_2
        fin = sorted(fin)
        return fin
