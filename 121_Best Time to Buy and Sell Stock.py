# Say you have an array for which the ith element is the price of a given stock on day i.
# #
# # If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# #
# # Note that you cannot sell a stock before you buy one.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # bruteforce method
        """
        max = 0
        flag = 0
        for m, val in enumerate(prices[1:]):
            # print(val,' : ',prices[m])
            if val > prices[m]:
                flag += 1
        if flag == 0:
            return max

        for i, val_i in enumerate(prices):
            for j, val_j in enumerate(prices[i:]):
                temp = val_j - val_i
                if max < temp:
                    max = temp
        return max
        """
        length = len(prices)
        if length == 0:
            return 0

        max = 0
        cur = prices[0]

        for i, val in enumerate(prices[1:]):
            if val > cur:
                temp = val - cur
                if temp > max:
                    max = temp
            else:
                cur = prices[i + 1]

        return max
s=Solution()
l=[10,9,8,7,6,5,4,3,2,1]
print(s.maxProfit(l))