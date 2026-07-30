class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)

        def dfs(sub, counter):
            nonlocal l
            if counter == l :
                return [sub]
            sub0 = sub
            sub1 = sub + [nums[counter]]
            return dfs(sub0, counter + 1) + dfs(sub1, counter + 1)
        
        return dfs([], 0)
        

            


