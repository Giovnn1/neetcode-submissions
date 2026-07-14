class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l == 1:
            return 0
        buy, sell = 0, 1
        m = 0
        while sell < l:
            m = max(m, prices[sell] - prices[buy])
            if prices[sell] < prices[buy]:
                buy = sell
            sell += 1
        return m
