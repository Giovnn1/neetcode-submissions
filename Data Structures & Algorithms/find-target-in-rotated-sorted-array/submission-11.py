class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find_min(n):
            if n[0] < n[len(n) -1]:
                return 0
            l, r = 0, len(n) - 1
            while r > l + 1:
                m = (r - l) // 2 + l
                if n[m] > n[l]:
                    l = m
                else:
                    r = m
            return r

        def explore(n, t):
            if n == [] or n[0] > t or n[len(n) - 1] < t:
                return -1
            l, r = 0, len(n) - 1
            while r > l + 1:
                m = (r - l) // 2 + l
                if n[m] == target:
                    return m
                if n[m] < target:
                    l = m
                else:
                    r = m
            if n[l] == target:
                return l
            if n[r] == target:
                return r
            return -1


        u = find_min(nums)
        if target >= nums[0]:
            if u == 0:
                return explore(nums, target)
            return explore(nums[:u], target)
        else:
            s =  explore(nums[u:], target)
            return s + u if s != -1 else -1
        












