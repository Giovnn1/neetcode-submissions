class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[len(nums) - 1] > nums[0]:
            return nums[0]

        l, r = 0, len(nums) - 1
        while r > l + 1:
            m = (r - l) // 2 + l
            if nums[m] > nums[l]:
                l = m
            else:
                r = m
        #if r == len(nums):
            
        return nums[r] #min(nums[l], nums[r])
            
            
