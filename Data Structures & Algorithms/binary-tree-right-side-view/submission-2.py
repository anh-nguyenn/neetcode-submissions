# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while len(queue) > 0:
            k = len(queue)
            for i in range(k):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right: 
                    queue.append(curr.right)
                if i == k - 1:
                    res.append(curr.val)
        return res

        

        