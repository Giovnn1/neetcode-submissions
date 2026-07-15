class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)


        seen = {ch : 0 for ch in s2}
        check = {ch : 0 for ch in s2}
        for ch in s2[:l1]:
            seen[ch] += 1
        for ch in s1:
            if ch not in check:
                return False
            check[ch] += 1
        
        if seen == check:
            return True


        for l in range(1, len(s2) - l1 + 1):
            seen[s2[l-1]] -= 1
            seen[s2[l + l1 -1]] += 1
            if seen == check:
                return True
        
        return False








