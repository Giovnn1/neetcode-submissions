class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        S = sum(nums)
        target = abs(target)
        if S < target or target < - S:
            return 0
        E = [[0 for _ in range(len(nums) + 1)] for _ in range(S + 1)]
        E[0][0] = 1
        #I want E[t][k] to contain the number of valid expression you can create with the integers in nums[:k] which sum to S
        for k in range(1, len(nums) + 1):
            for t in range(S + 1):
                E[t][k] += E[abs(t - nums[k-1])][k-1]
                E[t][k] += E[t + nums[k-1]][k-1] if t + nums[k-1] <= S else 0
        return E[target][-1]

                
