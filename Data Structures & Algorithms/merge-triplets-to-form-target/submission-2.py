class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tr = []
        for t in triplets:
            if (t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]):
                tr.append(t)
        if tr == []:
            return False
        #tr.sort()
        out = [0,0,0]
        for t in tr:
            out = [max(out[i], t[i]) for i in range(3)]
        
        return target == out

