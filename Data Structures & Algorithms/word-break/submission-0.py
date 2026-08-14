class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        L = len(s)
        dp = {0 : True}
        for l in range(1, L + 1):
            dp[l] = any([s[l - len(w) : l] == w and dp[l - len(w)] for w in wordDict])
        return dp[L]