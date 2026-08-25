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


        #note that a recursive approach like this is inefficient, since ti exponentially calls redundant subproblems, e.g. both dfs(1,0) and dfs(0,1) call dfs(1,1)
        #def dfs(i,j):
        #    if i == m - 1 or j == n - 1:
        #        return 1
        #    return dfs(i+1, j) + dfs(i, j+1)
        #
        #return dfs(0, 0)