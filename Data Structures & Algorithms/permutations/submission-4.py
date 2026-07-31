class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        curr =[]
        done = len(nums) * [False]

        def dfs(done):
            if len(curr) == len(nums):
                out.append(curr.copy())
                return
            for i in range(len(nums)):
                if not done[i]:
                    curr.append(nums[i])
                    done[i] = True
                    dfs(done)
                    curr.pop()
                    done[i] = False

        dfs(done)
        return out
            
            
            
