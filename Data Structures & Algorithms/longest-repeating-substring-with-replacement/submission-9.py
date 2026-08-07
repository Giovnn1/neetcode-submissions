class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxl = 0
        m = 0
        seen = {}

        for r in range(len(s)):
            seen[s[r]] = 1 + seen.get(s[r], 0)
            maxl = max(maxl, seen[s[r]])
            while r - l + 1 - maxl > k:
                seen[s[l]] -= 1
                l += 1
            m = max(m, r - l  + 1)
        return m



                    

                    


            


            

