class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        m = 0
        for sell in prices[1:]:
            m = max(sell - buy, m)
            if sell < buy:
                buy = sell
        return m

            

