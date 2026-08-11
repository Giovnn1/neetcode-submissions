class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        if L <= 2:
            return max(nums)
        money = L * [-1]
        money[L-1], money[L-2], money[L-3] = nums[L-1], nums[L-2], nums[L-3] + nums[L-1]

        for i in range(4, L + 1):
            money[L - i] = nums[L-i] + max(money[L-i+2], money[L-i+3])
        
        return max(money[0], money[1])
