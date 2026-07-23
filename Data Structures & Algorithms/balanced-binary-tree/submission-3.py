# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(R):
            nonlocal res

            if R is None:
                return 0
            l, r = dfs(R.left), dfs(R.right)
            res = res and (abs(l - r) <= 1)
            return max(l, r) + 1
        
        dfs(root)
        return res
            
