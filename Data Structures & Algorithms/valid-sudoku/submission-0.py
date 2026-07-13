class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_array(nums):
            seen = set()
            for n in nums:
                if n != '.':
                    if n in seen:
                        return False
                    else:
                        seen.add(n)
            return True
    
        def check_matrix(M):
            m = len(M)
            n = len(M[0])
            seen = set()
            for i in range(m):
                for j in range(n):
                    if M[i][j] != '.':
                        if M[i][j] in seen:
                            return False
                        else: seen.add(M[i][j])
            return True
        M = board
        for i in range(9):
            i_col = [M[k][i] for k in range(9)]
            if not ( check_array(M[i]) and check_array(i_col) ):
                return False
        
        for i in range(3):
            for j in range(3):
                N_pre = M[3*i: 3*i + 3]#   [M[k] for k in range(3*i, 3*i + 3)]
                N = [N_pre[k][3*j: 3*j + 3] for k in range(3)]
                if not check_matrix(N):
                    return False
        return True

                