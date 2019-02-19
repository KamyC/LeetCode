# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num_1=0
        num_2=0
        exp_1=0
        exp_2=0
        for i in a[::-1]:
            num_1+=int(i)*2**exp_1
            exp_1+=1
        for j in b[::-1]:
            num_2+=int(j)*2**exp_2
            exp_2+=1
        fin=num_1+num_2
        res=""
        while fin>0:
            mod=fin%2
            fin=int(fin/2)
            res+=str(mod)

        return res
a="1010"
b="1011"
s=Solution()
print(s.addBinary(a,b))
