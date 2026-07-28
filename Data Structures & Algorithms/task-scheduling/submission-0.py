class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        check = {t : 0 for t in tasks}
        for t in tasks:
            check[t] += 1
        situation = [[- check[t], t] for t in check]
        import heapq
        heapq.heapify(situation)
        added = []
        l = 0
        
        while situation:
            for _ in range(n + 1):
                if situation:
                    added.append(heapq.heappop(situation))
                    l += 1
            for a in added:
                if - a[0] > 1:
                    a[0] += 1
                    heapq.heappush(situation, a)
            if situation:
                idles = n + 1 - len(added) if n + 1 > len(added) else 0
                l += idles

            added = []

            
        return l



            

            





        

