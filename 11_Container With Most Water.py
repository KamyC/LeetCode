# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
# Example:
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length == 2:
            return min(height[0], height[1])
        else:
            l = 0
            r = length - 1
            fin = 0
            while l < r:
                if height[l] < height[r]:
                    fin = max(height[l] * (r - l), fin)
                    clh = height[l]
                    while height[l] <= clh:
                        l += 1
                        if l >= r:
                            return fin
                else:
                    fin = max(height[r] * (r - l), fin)
                    crh = height[r]
                    while height[r] <= crh:
                        r -= 1
                        if l >= r:
                            return fin
            return fin
s=Solution()
l=[2,3,4,5,18,17,6]
print(s.maxArea(l))