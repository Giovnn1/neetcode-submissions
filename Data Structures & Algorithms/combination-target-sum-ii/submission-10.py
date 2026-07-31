class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        curr = []
        candidates.sort()

        def dfs(i, tot):
            if sum(curr) == target:
                out.append(curr.copy())
                return
            if sum(curr) > target or i >= len(candidates):
                return
            curr.append(candidates[i])
            tot += candidates[i]
            dfs(i+1, tot + candidates[i])
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, tot)
            return

        dfs(0, 0)
        return out
