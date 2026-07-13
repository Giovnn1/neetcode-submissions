class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 1
        if l == 0:
            return 0
        s = set(nums)
        res = 0
        for n in nums:
            c = 0
            while n + c in s:
                c += 1
            res = max(res,c)
        return res



