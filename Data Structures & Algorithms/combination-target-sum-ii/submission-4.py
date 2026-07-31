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
            curr.append(candidates[i])
            dfs(i+1)
            curr.pop()
            j = 1
            while i + j < len(candidates) and candidates[i] == candidates[i + j]:
                i += 1
            dfs(i + j)
            return

        dfs(0)
        return out
