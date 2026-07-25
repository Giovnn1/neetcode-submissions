# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        left, right = self.rightSideView(root.left), self.rightSideView(root.right)

        res = [root.val]
        for i in range(len(right)):
            res.append(right[i])
        for j in range(len(right), len(left)):
            res.append(left[j])
        
        return res
        
        #def dfs(R):
        #    if R is None:
        #        return []
        #
        #    res = [R.val]
        #    left = dfs(R.left)
        #    right = dfs(R.right)
        #    m = min(len(left), len(right))
        #
        #    for i in range(m):
        #        res.append(right[i])
        #    for j in range(m, len(left)):
        #        res.append(left[i])
        #
        #    return res
        



