class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = matrix
        nrow, ncol = len(M), len(M[0])
        i, j = 0, 0
        while i < ncol and j < nrow:

            l, r = j, ncol - 1
            while M[i][r] < target:
                i += 1
                if i >= nrow:
                    return False
            while r > l + 1:
                mc = (r - l) // 2 + l
                if target == M[i][mc]:
                    return True
                if target > M[i][mc]:
                    l = mc
                else:
                    r = mc
            if M[i][r] == target or M[i][l] == target:
                return True
            
            u, d = i, nrow - 1
            while M[d][j] < target:
                j += 1
                if j >= ncol:
                    return False
            while d > u + 1:
                mr = (d - u) // 2 + u
                if target == M[mr][j]:
                    return True
                if target > M[mr][j]:
                    u = mr
                else:
                    d = mr
            if M[u][j] == target or M[d][j] == target:
                return True
            
            ncol, nrow = r, d
            i += 1
            j += 1

        return False                            

            


