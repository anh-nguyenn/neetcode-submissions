# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root_a, root_b):
            if not root_a and not root_b:
                return True
            if not root_a or not root_b: #either is none
                return False
            if root_a.val != root_b.val:
                return False
            return isSameTree(root_a.left, root_b.left) and isSameTree(root_a.right, root_b.right)
        
        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

