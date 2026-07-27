# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(R):
            if R is None:
                return (True, 1001, -1001)
            
            (c_l, min_l, max_l) = dfs(R.left)
            (c_r, min_r, max_r) = dfs(R.right)

            if not(c_l and c_r) or R.val <= max_l or R.val >= min_r:
                return (False, -1001, 1001)
            
            return (True, min(min_l, R.val), max(max_r, R.val))
            
        return dfs(root)[0]

        
        

        