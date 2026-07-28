class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        st = [- stone for stone in stones]
        heapq.heapify(st)
        while len(st) > 1:
            s1 = - heapq.heappop(st)
            s2 = - heapq.heappop(st)
            if s1 > s2:
                s1 -= s2
                heapq.heappush(st, - s1)
        return - st[0] if st else 0
            