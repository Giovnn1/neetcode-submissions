class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = numbers 
        l = len(n)
        for i in range(l):
            mid = (l - i) // 2
            if n[i] + n[mid] > target:
                j = i + 1
                while j < mid and n[i] + n[j] < target:
                    j += 1
                if n[i] + n[j] == target:
                    return [i + 1, j + 1]
            else:
                j = mid
                while j < l - 1 and n[i] + n[j] < target:
                    j += 1
                if n[i] + n[j] == target:
                    return [i + 1, j + 1]
        return

