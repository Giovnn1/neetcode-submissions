# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        anc = None

        def dfs(R):
            nonlocal anc

            if R is None:
                return {'p' : False, 'q': False}

            dl = dfs(R.left)
            dr = dfs(R.right)

            have_p = R.val == p.val or dl['p'] or dr['p']
            have_q = R.val == q.val or dl['q'] or dr['q']

            if have_p and have_q and (anc is None):
                anc = R
            
            return {'p' : have_p, 'q' : have_q}
        
            

        dfs(root)
        return anc


















            