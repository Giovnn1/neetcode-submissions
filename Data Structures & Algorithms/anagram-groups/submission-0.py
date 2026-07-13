class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            t = "".join(sorted(s))
            if t in dic.keys():
                dic[t] += [s]
            else:
                dic[t] = [s]
        return list(dic.values())
