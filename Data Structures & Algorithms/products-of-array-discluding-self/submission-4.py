class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pref = l * [0]
        suff = l * [0]
        pref[0], suff[0] = 1, 1
        for i in range(1, l):
            pref[i] = pref[i-1] * nums[i-1]
            suff[i] = suff[i-1] * nums[-i]
        res = l * [0]
        for i in range(l):
            res[i] = pref[i] * suff[l - i - 1]
        return res


