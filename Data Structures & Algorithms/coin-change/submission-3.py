class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #coins.sort()
        L  = len(coins)
        storage = (amount + 1) * [-1]
        storage[0] = 0
        #I want storage[k] to be coinChange(coins, k)
        for k in range(1, amount + 1):
            best = amount + 1
            for n in coins:
                best = min(best, 1 + storage[k - n]) if k - n >= 0 and storage[k - n] != - 1 else best
            storage[k] = best if best < amount + 1 else -1
        
        return storage[-1]


        