class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = set()
        for k in nums:
            if k in check:
                return k
            else:
                check.add(k)
        return