class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(l):
            if l == len(nums):
                res.append(subset.copy())
                return 
            subset.append(nums[l])
            dfs(l+1)
            subset.pop()
            dfs(l+1)
            return
        
        dfs(0)
        return res
        

            


