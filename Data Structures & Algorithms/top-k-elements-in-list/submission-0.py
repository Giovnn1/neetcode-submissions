class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        v = {}
        for n in nums:
            if n in v.keys():
                v[n] += 1
            else:
                v[n] = 1
        a = [[v[u], u] for u in v.keys()]
        a.sort()
        return [a[-k + i][1] for i in range(k)]

        