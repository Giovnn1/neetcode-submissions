class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1:
            return 0 if gas[0] >= cost[0] else -1
        l = 0
        while l < len(gas):
            if gas[l] < cost[l]:
                l += 1
                continue
            tank = gas[l] - cost[l]
            r = 0 if l == len(gas) - 1 else l + 1
            while tank >= 0:
                if r == l:
                    return l
                tank += gas[r] - cost[r]
                r = 0 if r == len(gas) - 1 else r + 1
            if r <= l:
                return -1
            l = r
        return -1
        




                

        

