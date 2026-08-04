class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []

        d = {'2' : ['a','b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5':['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        n = len(digits)
        res = []
        curr = []

        def dfs(k):

            if k == n:
                res.append("".join(curr.copy()))
                return
            for l in d[digits[k]]:
                curr.append(l)
                dfs(k+1)
                curr.pop()
            return
        dfs(0)
        return res 
