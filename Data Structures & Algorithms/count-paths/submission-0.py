class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = m * [[-1 for _ in range(n)]]
        ways[m-1] = n * [1]
        for row in ways:
            row[n-1] = 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                ways[i][j] = ways[i+1][j] + ways[i][j+1]
        
        return ways[0][0]
