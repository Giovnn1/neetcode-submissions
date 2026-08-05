class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        land_visited = set()
        n_islands = 0

        def land_explore(i,j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
                return 
            if grid[i][j] == "0" or (i,j) in land_visited:
                return
            
            land_visited.add((i,j))
            land_explore(i + 1, j)
            land_explore(i, j + 1)
            land_explore(i - 1, j)
            land_explore(i, j - 1)

            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not((i,j) in land_visited) and grid[i][j] == "1":
                    n_islands += 1
                    land_explore(i,j)
        
        
        return  n_islands            
            

