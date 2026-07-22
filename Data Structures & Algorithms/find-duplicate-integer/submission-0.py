class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for k in nums:
            if k in d:
                return k
            else:
                d[k] = 1
        return