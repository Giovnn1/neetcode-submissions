class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += str(len(s)) + "#" + s
        return out

    def decode(self, s: str) -> List[str]:
        l = len(s)
        i = 0
        out = []
        while i < l:
            j = i + 1
            while s[j] != "#":
                j += 1
            ll = int(s[i:j])
            w = s[j + 1 : j + ll + 1]
            out.append(w)
            i = j + ll + 1
        return out

