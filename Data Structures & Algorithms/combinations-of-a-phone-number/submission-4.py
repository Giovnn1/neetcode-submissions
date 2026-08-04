class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        d = {'2' : ['a','b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5':['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        def dfs(digs):

            if digs == "":
                return [""]
            out = []
            for l in d[digs[0]]:
                out.extend([ l + comb for comb in dfs(digs[1:])])
            return out

        if digits == "":
            return []
            
        return dfs(digits) 
