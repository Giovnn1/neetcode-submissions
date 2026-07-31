class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        curr = []
        candidates.sort()

        def dfs(i):
            if sum(curr) == target:
                out.append(curr.copy())
                return
            if sum(curr) > target or i >= len(candidates):
                return
            c = candidates[i]
            curr.append(c)
            dfs(i+1)
            curr.pop()
            while i < len(candidates) and candidates[i] == c:
                i += 1
            dfs(i)
            return

        dfs(0)
        sets = [comb for comb in out]
        return [[x for x in comb] for comb in sets]
