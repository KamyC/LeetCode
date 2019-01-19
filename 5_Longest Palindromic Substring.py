# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        list_1 = []
        temp = ''
        if s == s[::-1]:
            return s
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s == s[::-1]:
                return s
            else:
                return s[0]
        else:
            for i, val_i in enumerate(s):
                temp = val_i
                for j, val_j in enumerate(s[i + 1:]):
                    temp += val_j
                    if temp == temp[::-1]:
                        list_1.append(temp)
                        res = temp
        if list_1:
            for j, val_j in enumerate(list_1):
                if len(res) <= len(val_j):
                    res = val_j
            return res
        else:
            return temp
s=Solution()
print(s.longestPalindrome('babad'))
print(s.longestPalindrome('cbbd'))
print(s.longestPalindrome('ac'))
print(s.longestPalindrome('abcda'))
