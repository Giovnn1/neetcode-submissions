class Solution:
    def rob(self, nums: List[int]) -> int:
        #the idea is tha no paths contain both nums[0] and nums[len(nums)-1], so we run the rob1 (see previous exercise) on nums[1:] and nums[:len(nums) - 1]
        def rob1(n):
            L = len(n)
            if L <= 2:
                return max(n)
            m1, m2, m3 = n[L-1], n[L-2], n[L-3] + n[L-1]
            for i in range(4, L+1):
                m = n[L-i] + max(m2, m1)
                m3, m2, m1 = m, m3, m2
            return max(m3, m2)
        
        return max(rob1(nums[1:]), rob1(nums[:len(nums)-1])) if len(nums) > 2 else max(nums)