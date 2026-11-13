class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        storage = set()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    storage.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                else:
                    if nums[i] + nums[left] + nums[right] > 0:
                        right -= 1
                    else:
                        left += 1
        return [list(t) for t in storage]