class MedianFinder:

    def __init__(self):
        self.flow = []

    def addNum(self, num: int) -> None:
        self.flow.append(num)
        self.flow.sort()

    def findMedian(self) -> float:
        L = len(self.flow)
        if L % 2 == 1:
            return self.flow[int((L-1) / 2)]
        else:
            m1 = self.flow[(L-1) // 2]
            m2 = self.flow[int(L/2)]
            return (m1 + m2) / 2
        