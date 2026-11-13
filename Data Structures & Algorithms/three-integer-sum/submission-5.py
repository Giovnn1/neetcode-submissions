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
            

















    #def threeSum(self, nums: List[int]) -> List[List[int]]:
    #    nums.sort()
    #    l = len(nums)
    #    d = {}
    #    for i in range(l):
    #        left = i + 1
    #        right = l - 1
    #        while left < right:
    #            if nums[i] + nums[left] + nums[right] < 0:
    #                left += 1
    #                continue
    #            if nums[i] + nums[left] + nums[right] > 0:
    #                right -= 1
    #                continue
    #            d[(nums[i], nums[left], nums[right])] = 1
    #            left += 1
    #            right -= 1
    #    return [list(k) for k in d.keys()]
            

              





