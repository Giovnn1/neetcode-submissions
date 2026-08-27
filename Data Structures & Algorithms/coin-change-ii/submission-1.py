class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        W = [[0 for _ in range(len(coins) + 1)] for _ in range(amount + 1)]
        #I want W[a][k] to contain the number of ways to write a with coins[: k]
        #W[a][0] = 0 for all a>0 bc you cannot make any amount > 0with no coins
        #W[0] = (len(coins) + 1) * [1] 
        for j in range(len(coins) + 1):
            W[0][j] = 1
        for a in range(1, amount + 1):
            for k in range(1, len(coins) + 1):
                W[a][k] += W[a][k-1] if a - coins[k-1] < 0 else W[a][k-1] + W[a - coins[k-1]][k]

        return W[-1][-1]
