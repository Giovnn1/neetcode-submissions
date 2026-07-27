# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(R, m):
            if R is None:
                return 0
            
            if R.val < m:
                N = dfs(R.left, m) + dfs(R.right, m)
            else:
                N = dfs(R.left, R.val) + dfs(R.right, R.val) + 1
            
            return N
        
        return dfs(root, - 100)