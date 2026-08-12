class Solution:
    def numDecodings(self, s: str) -> int:
        L = len(s)
        if L == 0 or s[0] == "0":
            return 0
        D = 1
        ND = 0
        for i in range(L - 2, -1, -1):
            if s[i] == "0" and s[i-1] not in ("1", "2"): #we have already excluded the case s[0] == "0"
                return 0
            
            elif s[i] == "2"and  s[i+1] not in ("0", "7", "8", "9") and (i+2 >= L or s[i+2] != "0"):
                    D, ND = D + ND, D
            
            elif s[i] == "1" and s[i+1] != "0" and (i+2 >= L or s[i+2] != "0"):
                D, ND = D + ND, D
            else:
                D, ND = D + ND, 0
        return D + ND  


