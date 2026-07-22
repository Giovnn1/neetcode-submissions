class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #for pre_ind in nums: #possiamo vedere gli elementi di nums come indici
        #    ind = abs(pre_ind) - 1
        #    if nums[ind] < 0:
        #        return - nums[ind]
        #    nums[ind] *= -1
        for num in nums :
            idx = abs(num) - 1
            if nums[idx] < 0 :
                return abs(num)
            nums[idx] *= -1
        return -1
