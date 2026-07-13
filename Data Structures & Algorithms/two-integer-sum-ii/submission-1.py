class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = numbers
        l = len(n)
        up = l - 1
        i1 = 0
        for i1 in range(l):
            i2 = i1 + 1
            while i2 < up and n[i1] + n[i2] < target:
                i2 += 1
            if n[i1] + n[i2] == target:
                return [i1 + 1, i2 + 1]
            elif n[i1] + n[i2] > target:
                up = i2
        return 
