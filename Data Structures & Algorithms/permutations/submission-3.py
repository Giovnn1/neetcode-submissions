class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        curr =[]

        def dfs(v):
            if len(v) == 1:
                out.append(curr + v)
                return
            for i in range(len(v)):
                curr.append(v[i])
                dfs(v[ : i] + v[i + 1 :])
                curr.pop()

        dfs(nums)
        return out
            
            
            
