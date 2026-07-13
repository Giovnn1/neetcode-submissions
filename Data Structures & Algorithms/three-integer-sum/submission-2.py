class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        nums.sort()
        res = [] #[[1,1,1]]
        for i in range(l):


            #check che non ho capito, ma devo anda avanti
            if i > 0 and nums[i] == nums[i-1]:
                continue


            left, right  = i + 1, l - 1
            #while left < right and nums[i] == res[-1][0] and nums[left] == res[-1][1] and nums[right] == res[-1][2]:
            #    left += 1
            while left < right:
                #while nums[i] == res[-1][0] and nums[left] == res[-1][1]:
                #    left += 1
                tS = nums[i] + nums[left] + nums[right]
                if tS < 0:
                    left += 1
                    continue
                if tS > 0:
                    right -= 1
                    continue
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
        return res
                





