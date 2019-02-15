# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5

class Solution:
    def lengthOfLastWord(self, s: 'str') -> 'int':
        l=[]
        l=s.split()
        if len(l)==0:
            return 0
        res=l[-1]
        return len(res)
s=Solution()
str="Hello World"
print(s.lengthOfLastWord(str))

