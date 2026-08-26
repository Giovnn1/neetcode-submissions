class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        prs = l * [0] #prs[i] contains masProfit(prices[i:])
        for i in range(l-2, -1, -1):
            for j in range(i + 1, l):
                pr = prices[j] - prices[i]
                prs[i] = max(pr, prs[i]) if j + 2 >= l else max(pr + prs[j + 2], prs[i])
            prs[i] = max(prs[i], prs[i+1]) 
        return prs[0]