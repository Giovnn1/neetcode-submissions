class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        for _ in range(len(nums)):
            if r <= l:
                return r if nums[r] == target else -1
            m = (r + l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1