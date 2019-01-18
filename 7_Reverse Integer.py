# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        class Solution:
            def reverse(self, x):
                """
                :type x: int
                :rtype: int
                """
                l = []
                if x < 0:
                    abs_x = abs(x)
                    num_str = str(abs_x)
                else:
                    num_str = str(x)

                for i, val in enumerate(num_str):
                    l.append(val)
                l.reverse()

                if x < 0:
                    l.insert(0, '-')

                res = ''
                for j, val in enumerate(l):
                    res += val
                res = int(res)
                if res >= -2 ** 31 and res <= 2 ** 31 - 1:
                    return res
                else:
                    return 0
