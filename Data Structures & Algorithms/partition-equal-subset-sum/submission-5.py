class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        if sum(nums) % 2 != 0:
            return False
        
        S, l = int(sum(nums)/2), len(nums)
        reachable = {0}

        for i in range(l - 1, -1, -1):
            to_add = {0}
            for t in reachable:
                if nums[i] + t <= S:
                    to_add.add(nums[i] + t)
            reachable |= to_add
        return S in reachable
        

