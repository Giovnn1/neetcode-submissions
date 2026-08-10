class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        L = len(cost)
        if L <= 2:
            return min(cost)
            
        price = L * [-1]
        #price[-i] will be the price of climbing the stairs when you start at cost[-i]
        price[-1] = cost[-1]
        price[-2] = cost[-2]

        for i in range(3, L + 1):
            price[-i] = cost[-i] + min(price[-i + 1], price[-i + 2])
        
        return min(price[0], price[1])




