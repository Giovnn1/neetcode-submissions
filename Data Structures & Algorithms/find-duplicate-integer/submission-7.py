class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for pre_ind in nums: #possiamo vedere gli elementi di nums come indici
            ind = abs(pre_ind) - 1
            if nums[ind] < 0:
                return abs(pre_ind)
            nums[ind] *= -1
        