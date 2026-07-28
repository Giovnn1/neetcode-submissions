class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq

        #dist = [p[0]**2 + p[1]**2 for p in points]
        D = {p[0]**2 + p[1]**2 : [] for p in points}
        for p in points:
            D[p[0]**2 + p[1]**2].append(p)
        
        
        answer = []
        dist = [d for d in D.keys()]
        heapq.heapify(dist)

        while len(answer) < k:
            d = heapq.heappop(dist)
            answer += D[d]
        
        return answer[:k]
        
        
            
        

        

