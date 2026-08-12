class Solution:
    def countSubstrings(self, s: str) -> int:
        L = len(s)
        if L <= 1:
            return 1

        out = 0
        dp = [[False for j in range(L)] for i in range(L)]

        for i in range(L - 1, -1, -1):
            for j in range(i, L):
                if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    out += 1
        return out