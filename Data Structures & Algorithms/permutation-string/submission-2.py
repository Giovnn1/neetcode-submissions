class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l1, l2 = len(s1), len(s2)
        if l2 < l1:
            return False

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        d1 = {ch : 0 for ch in alphabet}
        dl = {ch : 0 for ch in alphabet}

        for i in range(l1):
            d1[s1[i]] += 1
            dl[s2[i]] += 1
        if d1 == dl:
            return True

        for l in range(1, l2 - l1 + 1):
            dl[s2[l - 1]] -= 1 #remove the new excluded
            dl[s2[l + l1 - 1]] += 1 #add the new included
            if dl == d1:
                return True

        return False





