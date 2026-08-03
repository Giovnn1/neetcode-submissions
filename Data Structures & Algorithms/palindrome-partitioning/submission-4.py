class Solution:

    def is_palindromic(self, w):
        L = len(w)
        for u in range(L // 2):
            if w[u] != w[L - 1 - u]:
                    return False
        return True

    def partition(self, s: str) -> List[List[str]]:

        def dfs(word):
            if not word:
                return [[]]
            if len(word) == 1:
                return [[word]]

            out = []

            for j in range(1, len(word) + 1):
                if self.is_palindromic(word[:j]):
                    #new = [[word[:j]] + l for l in dfs(word[j:])]
                    out.extend([[word[:j]] + l for l in dfs(word[j:])])
                    #l = dfs(word[j:])
                    #l.append(word[j:])
                    #out.append(l)
            
            return out
        
        return dfs(s)