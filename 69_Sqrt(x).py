# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
# Input: 4
# Output: 2
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        exp=0
        while 2**exp<x:
            exp+=1
        # print(exp)
        low=2**(int(exp/2)-1)
        high=2**(int((exp-1)/2)+1)

        # print(low, high)
        if low==high:
            return low
        for i in range(low,high):
            a=i**2
            b=(i+1)**2
            if a==x:
                return i
            if b==x:
                return i+1
            if a<x<b:
                return i


s=Solution()
print(s.mySqrt(3))


