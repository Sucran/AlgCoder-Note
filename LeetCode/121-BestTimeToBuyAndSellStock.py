class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_num = 100000000
        max_profit = 0
        for i in range(len(prices)):
            min_num = min_num if min_num < prices[i] else prices[i]
            profit = prices[i] - min_num
            if profit > max_profit:
                max_profit = profit
        return max_profit