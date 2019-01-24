# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L=[]
        length=len(s)
        # keys={'{':}

        # for i,val in enumerate(s):
        #     L.append(val)

        if length%2!=0 and length>0 :
            return False
        else:
            for i, val in enumerate (s):

                if val==')':
                    if len(L) != 0:
                        temp=L[-1]
                        if temp=='(':
                            L.pop()
                        else:
                            L.append(val)
                    else:
                        return False
                elif val==']':
                    if len(L) != 0:
                        temp=L[-1]
                        if temp=='[':
                            L.pop()
                        else:
                            L.append(val)
                    else:
                        return False
                elif val=='}':
                    if len(L) != 0:
                        temp=L[-1]
                        if temp=='{':
                            L.pop()
                        else:
                            L.append(val)
                    else:
                        return False
                else:
                    L.append(val)
            if len(L)==0 :
                # print(L)
                return True
            else:
                # print(L)
                return False

s=Solution()
# print(s.isValid('()'))
# print(s.isValid('()[]{}'))
# print(s.isValid('(]'))
print(s.isValid("){"))



        
