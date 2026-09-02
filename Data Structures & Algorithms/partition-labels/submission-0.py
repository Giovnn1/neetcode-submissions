class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        v = {c : -1 for c in s}
        for i in range(len(s)):
            v[s[i]] = i
        out = []
        l, r = 0, v[s[0]]
        while True:
            i = l
            while i < r:
                i += 1
                r = max(r, v[s[i]])
            out.append(r - l + 1)
            l = r + 1
            if l >= len(s):
                return out
            r = v[s[l]]
