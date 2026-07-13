class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        p, zero_ind = 1, None
        for i in range(l):
            if nums[i]:
                p *= nums[i]
            else:
                if zero_ind is not None:
                    return l * [0]
                else:
                    zero_ind = i
        if zero_ind is not None:
            return zero_ind * [0] + [p] + (l - zero_ind - 1) * [0]
        else:
            return [p//n for n in nums]

