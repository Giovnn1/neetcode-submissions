class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        len_s = len(s)
        l = 0
        m = 1
        freq = {ch : 0 for ch in s}
        freq[s[0]] += 1
        max_f = 1

        for r in range(1, len_s):
            freq[s[r]] += 1
            max_f = max(freq.values())

            while r - l + 1 - max_f > k:
                freq[s[l]] -= 1
                #max_f = max(freq.values())
                l += 1
            m = max(m, r - l + 1)

        return m


            

