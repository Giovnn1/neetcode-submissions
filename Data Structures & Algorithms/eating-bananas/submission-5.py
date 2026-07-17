class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def time(p, speed):
            return sum((-(-n // speed) for n in p))

        l, r = 1, max(piles)
        while r > l:
            m = (r - l) // 2 + l
            if time(piles, m) <= h:
                r = m
            else:
                l = m + 1
        return l
        






