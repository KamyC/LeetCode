# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
#
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:
#
# Coud you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        l1=[]
        if x >= 0:
            while x > 0:
                l1.append(x % 10)
                x = x // 10
            l2 = list(l1)
            l1.reverse()
            if l2==l1:
                return True
            else :
                return False
        else:
            return False


