class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        curr = 0
        nrow, ncol = len(grid), len(grid[0])

        def dfs(i,j):
            nonlocal curr
            if i >= nrow or j >= ncol or i < 0 or j < 0:
                return 
            if grid[i][j] == 0:
                return
            
            curr += 1
            grid[i][j] = 0

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

            return

        for i in range(nrow):
            for j in range(ncol):
                dfs(i,j)
                max_area = max(max_area, curr)
                curr = 0
        
        return max_area
