# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def checkTarget(root, targetSum):
            if not root:
                return False
            # check leaf
            if not root.left and not root.right:
                return root.val == targetSum
            
            # recursive
            return (checkTarget(root.left, targetSum - root.val) or checkTarget(root.right, targetSum - root.val))
        
        return checkTarget(root, targetSum)
            

        