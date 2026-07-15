# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        if not root:
            return None
        queue.append(root)
        while len(queue) > 0:
            for _ in range(len(queue)):
                no = queue.popleft()
                no.left, no.right = no.right, no.left
                if no.left:
                    queue.append(no.left)
                if no.right:
                    queue.append(no.right)
        return root
        