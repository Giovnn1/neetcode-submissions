class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        seen = {ch : 0 for ch in s}
        l, m = 0, 0

        for r in range(0, len(s)):
            if seen[s[r]] > 0:
                while s[l] != s[r]:
                    seen[s[l]] -= 1
                    l += 1
                seen[s[l]] -= 1
                l += 1          
            seen[s[r]] += 1
            m = max(m, r - l + 1)
        return m





