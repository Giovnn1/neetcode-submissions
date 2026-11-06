class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        D = {ch : 0 for ch in s2}
        check = {ch : 0 for ch in s2}
        for ch in s1:
            if ch in D:
                D[ch] += 1 
            else:
                return False
                
        for i in range(l1):
            check[s2[i]] += 1
        if check == D:
            return True

        for i in range(1, l2 - l1 + 1):
            check[s2[i-1]] -= 1
            check[s2[i + l1 - 1]] += 1
            if check == D:
                return True
        return False











