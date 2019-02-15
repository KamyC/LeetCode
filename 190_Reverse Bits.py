# Reverse bits of a given 32 bits unsigned integer.
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        num_str = ""
        while n:
            temp = str(n % 2)
            num_str += temp
            n = n / 2
        res = 0
        exp = 0
        # print(num_str)
        length = len(num_str)
        if 32 - length > 0:
            zeros = 32 - length
            while zeros > 0:
                num_str += "0"
                zeros -= 1

        # print(num_str)
        for i in num_str[::-1]:
            res += int(i) * 2 ** exp
            exp += 1
        return res