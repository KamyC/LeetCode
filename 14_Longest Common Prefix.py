# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(set(strs)) >= 2:
            final = ''
            len_list = []
            pre_list = [''] * len(strs)
            for i, val in enumerate(strs):
                len_list.append(len(val))
            min_length = min(len_list)
            set_l = []
            list_l = []
            for i in range(min_length):
                for j, val in enumerate(strs):
                    pre_list[j] += val[i]
                    set_l = set(pre_list)
                if len(set_l) <= 1:
                    list_l = list(set_l)
                else:
                    break;
            if len(set(list_l)) > 1:
                return ''
            else:
                for i, val in enumerate(list_l):
                    final = val
                return final
        elif len(set(strs)) == 1:
            return strs[0]
        else:
            return ''

input_list=["ab","a"]
s=Solution()
print(s.longestCommonPrefix(input_list))