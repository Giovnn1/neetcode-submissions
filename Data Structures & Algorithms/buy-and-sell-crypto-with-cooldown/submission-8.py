class Solution:
    def maxProfit(self, prices: List[int]) -> int: #prob you can also do it with O(1) memory
        l = len(prices)
        profit = l * [0] #profit[i] contains maxProfit(prices[i:])
        best_sell = prices[-1]
        #best_sell is the max profit you can achieve starting from time if if you are forced to buy at time i (without counting the price at time i)
        for i in range(l - 2, -1, -1):
            profit[i] = max(profit[i + 1], best_sell - prices[i])
            best_sell = max(best_sell, prices[i]) if i + 2 >= l else max(best_sell, prices[i] + profit[i+2])

        return profit[0]  