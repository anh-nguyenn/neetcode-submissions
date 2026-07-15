# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0

        def deleteSmallest(root):
            if not root.left:
                self.res = root.val
                return root.right
            root.left = deleteSmallest(root.left)
            return root

        for _ in range(k):
            root = deleteSmallest(root)
        return self.res
        