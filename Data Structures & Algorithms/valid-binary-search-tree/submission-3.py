# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        if root:
            queue.append((root, float('-inf'), float('inf')))
        while queue:
            for _ in range(len(queue)):
                nd, low, high = queue.popleft()
                if not (low < nd.val < high):
                    print(nd.val, low, high)
                    return False
                if nd.left:
                    queue.append((nd.left, low, nd.val))
                if nd.right:
                    queue.append((nd.right, nd.val, high))
        return True
                

        