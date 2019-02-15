# Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        while n>0:
            temp=n%2
            if temp == 1:
                count+=1
            n=n/2
        return count