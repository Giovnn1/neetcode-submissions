# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth_smallest = - 1

        def dfs(R):
            nonlocal k
            nonlocal kth_smallest

            if R is None or k == 0:
                return

            dfs(R.left)
            if k > 0:
                kth_smallest = R.val
                k -= 1
                dfs(R.right)

            return

        dfs(root)
        return kth_smallest

            
            


