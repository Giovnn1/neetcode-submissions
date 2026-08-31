class Solution:
    def canJump(self, nums: List[int]) -> bool:
        s = 0
        while s < len(nums) - 1:
            if nums[s] == 0:
                return False
            jump, i_land = -1, -1
            for i in range(1, min(nums[s] + 1, len(nums) - s)):
                if i + nums[s + i] > jump + nums[i_land] or (i + nums[s + i] == jump + nums[i_land] and i > jump):
                    jump, i_land = i, s + i
            s = i_land
        
        return True
            