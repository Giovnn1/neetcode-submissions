class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        t1, t2 = text1, text2
        M = [[0 for _ in range(l2)] for _ in range(l1)]
        #I want M[i][j] to be the longest common substring of text1[i:] and text2[j:]
        M[l1 - 1][l2 -1] = 1 if text1[l1 - 1] == text2[l2 - 1] else 0
        for j in range(l2 - 2, -1, -1):
            M[l1 - 1][j] = 1 if t1[l1 - 1] == t2[j] or M[l1 - 1][j + 1] == 1 else 0
        for i in range(l1 - 2, -1, -1):
            M[i][l2 - 1] = 1 if t1[i] == t2[l2 - 1] or M[i + 1][l2 - 1] == 1 else 0
        
        for i in range(l1 - 2, -1, -1):
            for j in range(l2 - 2, -1, -1):
                if t1[i] == t2[j]:
                    M[i][j] = 1 + M[i + 1][j + 1]
                else:
                    M[i][j] = max(M[i + 1][j], M[i][j + 1])
        
        return M[0][0]

