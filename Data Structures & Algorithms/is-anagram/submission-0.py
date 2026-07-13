class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        voc_s = {}
        voc_t = {}
        for l in s:
            if l in voc_s.keys():
                voc_s[l] +=1
            else:
                voc_s[l] = 1
        for l in t:
            if l in voc_t.keys():
                voc_t[l] += 1
            else:
                voc_t[l] = 1
        return voc_s == voc_t
        
