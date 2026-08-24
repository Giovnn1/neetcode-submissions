class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        longest = l * [-1]
        for i in range(l - 1, -1, -1):
            m = 1
            for j in range(i + 1, l):
                if nums[i] < nums[j]:
                    m = max(longest[j] + 1, m)
            longest[i] = m
        return max(longest)




                  
                

