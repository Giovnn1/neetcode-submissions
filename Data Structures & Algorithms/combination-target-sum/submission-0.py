class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(k, curr, tot):
            if tot == target:
                res.append(curr.copy())
                return
            if tot > target:
                return
            if k >= len(nums):
                return 
            curr.append(nums[k])
            dfs(k, curr, tot + nums[k])
            curr.pop()
            dfs(k + 1, curr, tot)
            return
        
        dfs(0, [], 0)
        return res


