# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(R):
            if R is None:
                return [0,0]
            return [max(dfs(R.left)[0], dfs(R.right)[0], dfs(R.left)[1] + dfs(R.right)[1] + 1), max(dfs(R.left)[1], dfs(R.right)[1]) + 1]
        
        return dfs(root)[0] - 1