class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0
        if length == 1:
            return 0
        max = 0
        for i, val in enumerate(prices[1:]):
            if val > prices[i]:
                temp = val - prices[i]
                max += temp
        return max
