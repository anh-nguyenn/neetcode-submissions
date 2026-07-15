# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res_p = []
        res_q = []

        def selialize(root, res):
            if not root:
                res.append(None)
                return None
            res.append(root.val)
            selialize(root.left, res)
            
            
            selialize(root.right, res)
        
        selialize(p, res_p)
        selialize(q, res_q)
        return res_p == res_q