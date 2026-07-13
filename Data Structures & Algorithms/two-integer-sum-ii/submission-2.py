class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = numbers
        l = len(n)
        for i in range(l):
            need = target - n[i]
            mid = (l - i) // 2
            if n[mid] > need:
                for j in range(i + 1, mid):
                    if n[j] == need:
                        return [i+1, j+1]
            else:
                for j in range(mid, l):
                    if n[j] == need:
                        return [i+1, j+1]
        return 
