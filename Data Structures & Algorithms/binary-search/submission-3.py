class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if target == nums[r]:
            return r
        for _ in range( 2 * len(nums)):
            m = (r - l) // 2 +  l
            if nums[m] == target:
                return m
            else:
                if nums[m] > target:
                    r = m
                else:
                    l = m
        return -1