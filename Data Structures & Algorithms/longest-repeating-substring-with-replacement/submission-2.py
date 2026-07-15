class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {ch : 0 for ch in s}
        l = 0
        most_common = 0
        m = 0
        
        for r in range(len(s)):
            seen[s[r]] += 1
            most_common = max(most_common, seen[s[r]])

            while r - l + 1 - most_common > k:
                seen[s[l]] -= 1
                l += 1
            
            m = max(r - l + 1, m)

        return m


            


            

