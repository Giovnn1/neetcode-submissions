class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        loc = []
        l = len(nums)
        for i in range(l):
            if nums[i] == 0:
                loc.append(i)
                if len(loc) >= 2:
                    return l * [0]
        from math import prod
        if len(loc) >= 1:
            z = loc[0]
            return z * [0] + [prod(nums[ : z] + nums[z + 1 : ])] + (l - z - 1) * [0]
        p = prod(nums)
        return [int(p/n) for n in nums]