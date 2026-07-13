class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        #from collections import defaultdict
        #d = defaultdict(int)
        d = {}
        for i in range(l):
            left = i + 1
            right = l - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                    continue
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                    continue
                #if nums[i] + nums[left] + nums[right] == 0:
                d[(nums[i], nums[left], nums[right])] = 1
                left += 1
                right -= 1
        return [list(k) for k in d.keys()]
            

              





