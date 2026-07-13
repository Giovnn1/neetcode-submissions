class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        while nums:
            n = nums.pop()
            if n in seen:
                return True
            else:
                seen.add(n)
        return False 