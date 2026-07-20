class TimeMap:


    def __init__(self):
        self.d = {}

    def biggest_smaller(self, n, target):
        #target = [target, 0]
        if target < n[0][0]:
            return -1
        if target >= n[len(n) - 1][0]:
            return len(n) - 1

        l, r = 0, len(n) - 1
        while r > l:
            m = (r - l) // 2 + l
            if n[m][0] <= target:
                best = m
                l = m + 1
            else:
                r = m
        return best

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            u = self.biggest_smaller(self.d[key], timestamp)
            self.d[key] = self.d[key][: u+1] + [[timestamp, value]] +  self.d[key][u+1 :]
        else:
            self.d[key] = [[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        u = self.biggest_smaller(self.d[key], timestamp)
        return self.d[key][u][1] if u != -1 else ""
        
