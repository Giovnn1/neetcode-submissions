class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MAX, current = nums[0], 0
        for r in range(len(nums)):
            current += nums[r]
            MAX = max(MAX, current)
            current = max(current, 0)
        return MAX

