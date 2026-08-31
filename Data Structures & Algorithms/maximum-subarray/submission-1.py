class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MAX = nums[0]
        current = 0
        for r in range(len(nums)):
            current += nums[r]
            MAX = max(MAX, current)
            if current < 0:
                current = 0
        return MAX

