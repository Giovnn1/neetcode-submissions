class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while r > l + 1:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m
            else:
                l = m
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1