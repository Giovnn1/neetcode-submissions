class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        L = len(nums)
        l = 0
        maxprod = nums[0]
        while l < L:
            r, prod = l, 1
            i_lastneg = -1
            i_firstneg = -1
            p_firstneg = 0
            while r < L and prod != 0:
                prod *= nums[r]
                maxprod = max(maxprod, prod)
                if nums[r] < 0:
                    i_lastneg = r if i_lastneg < 0 else -1
                    p_firstneg = prod if i_firstneg < 0 else p_firstneg
                    i_firstneg = r if i_firstneg < 0 else i_firstneg
                r += 1
            if prod == 0:
                l = r
            if prod < 0:
                maxprod = max(maxprod, prod / p_firstneg) if r > l + 1 else maxprod
                l = i_lastneg + 1
            if prod > 0:
                l = L
        return int(maxprod)



