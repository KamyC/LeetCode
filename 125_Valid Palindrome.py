# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        length = len(s)
        if length == 0:
            return True

        l_1 = []
        l_2 = []
        for i in range(length):
            if s[i].isalpha() or s[i].isdigit():
                # print(s[i])
                l_1.append(s[i])
                l_2.append(s[i])
        l_1.reverse()
        return l_2 == l_1