class Solution:
    def jump(self, nums: List[int]) -> int:
        s, count = 0, 0
        while s < len(nums) - 1:
            jump = 0
            for i in range(1, min(nums[s] + 1, len(nums) - s)):
                if i + nums[s + i] >= jump + nums[s + jump] or s + i == len(nums) - 1:# or (i + nums[i] == jump + nums[i_land] and i > jump):
                    jump = i
            s += jump
            count += 1
        return count