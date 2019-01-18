# Given a string, find the length of the longest substring without repeating characters.

# Example 1:
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length=1
        s1 = ''
        l=[]
        for i,val_i in enumerate(s):
            s1+=val_i
            l.append(len(s1))
            for j,val_j in enumerate(s[i+1:]):
                if s1.find(val_j)<0:
                    s1+=val_j
                else:
                    if len(s1)>length:
                        length=len(s1)
                        l.append(length)
                    break
                l.append(len(s1))
            s1=''
        if s:
            return max(l)
        else:
            return 0
s= Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))





