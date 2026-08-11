class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        if L <= 2:
            return max(nums)

        m1, m2, m3 = nums[L - 1], nums[L - 2], nums[L - 3] + nums[L - 1]

        for i in range(4, L + 1):
            m = nums[L - i] + max(m2, m1)
            m3, m2, m1 = m, m3, m2
        
        return max(m3, m2)

