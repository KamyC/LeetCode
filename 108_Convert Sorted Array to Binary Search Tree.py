# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        length = len(nums)

        def recursion(nums, left, right):
            mid = (left + right) / 2
            root = TreeNode(nums[mid])
            if left < mid:
                root.left = recursion(nums, left, mid - 1)
            if right > mid:
                root.right = recursion(nums, mid + 1, right)
            return root

        return recursion(nums, 0, length - 1)


