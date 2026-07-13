class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = 9 * [0]
        cols = 9 * [0]
        mats = 9 * [0]

        for r in range(9):
            for c in range(9):
                
                if board[r][c] == '.':
                    continue
                
                val = int(board[r][c]) - 1

                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & mats[3 * (r//3) + c//3]:
                    return False

                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                mats[r//3 + c//3] |= (1 << val)

        return True