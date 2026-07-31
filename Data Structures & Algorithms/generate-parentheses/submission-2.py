class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr, out = [], []

        def dfs(op, cl):
            if cl > op or op > n or cl > n:
                return
            if op == n and cl == n:
                out.append("".join(curr))
                return
            curr.append("(")
            dfs(op + 1, cl)
            curr.pop()
            curr.append(")")
            dfs(op, cl + 1)
            curr.pop()

        dfs(0, 0)
        return out       
            
            