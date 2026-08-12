class Solution:
    def longestPalindrome(self, s: str) -> str:
        #the optimal approach here is to find all even and odd palindromic substrings and then returning the longest one. Anyway, I'm going for the dynamic programmic approach here for pedagogical purposes.
        L = len(s)
        if L < 2:
            return s
        dp = [[False for j in range(L)] for i in range(L)]
        #df[i][j] will be True iff s[i:j + 1] is palindromic
        longest_i = longest_j = 0
        for i in range(L - 1, -1, -1):
            for j in range(i, L):
                if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j - i > longest_j - longest_i:
                        longest_i, longest_j = i, j
        return s[longest_i:longest_j + 1]


        