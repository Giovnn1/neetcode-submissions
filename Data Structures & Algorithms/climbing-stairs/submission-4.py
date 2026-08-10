class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        W = n * [0]
        W[0], W[1] = 1, 2
        for i in range(2, n):
            W[i] = W[i-1] + W[i-2]
        return W[-1]