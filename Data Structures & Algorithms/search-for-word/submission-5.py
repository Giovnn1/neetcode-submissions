class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #vword = [l for l in word]
        #so_far = []7
        L = len(word)

        def dfs(i, j, path, i_needed, l):
            
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or (i,j) in path:
                return False
            if board[i][j] != word[i_needed]:
                return False
            path.add((i,j))

            if l + 1 == L or dfs(i + 1, j, path, i_needed + 1, l+1) or dfs(i - 1, j, path, i_needed + 1, l+1) or dfs(i, j + 1, path, i_needed + 1, l+1) or dfs(i, j - 1, path, i_needed + 1, l+1):
                return True
            
            path.remove((i,j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, set(), 0, 0):
                    return True
                    
        return False


