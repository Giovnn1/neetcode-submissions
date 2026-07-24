# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)
        trasv = [[root.val]]
        m = min(len(left), len(right))
        for i in range(m):
            trasv.append(left[i] + right[i])
        for i in range(m, len(left)):
            trasv.append(left[i])
        for i in range(m, len(right)):
            trasv.append(right[i])
        return trasv