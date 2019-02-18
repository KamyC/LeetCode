# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length=len(s)
        l_1=[]
        for i in range (length):
            if not s[i].isspace():
                l_1.append(s[i])
        l_1.reverse()
        print(l_1)