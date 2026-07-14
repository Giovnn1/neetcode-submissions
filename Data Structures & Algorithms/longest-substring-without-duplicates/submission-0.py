class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l <= 1:
            return l
        left = 0
        m = 0
        check = {}

        for right in range(l):
            if s[right] in check:
                left = max(left, check[s[right]] + 1)
            check[s[right]] = right
            m = max(m, right - left + 1)
        return m


