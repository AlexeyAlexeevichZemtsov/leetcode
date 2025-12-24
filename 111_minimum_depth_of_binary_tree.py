# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def _isDegenerate(self, node: TreeNode) -> bool:
        while node:
            if node.left and node.right:  # Два ребёнка → не вырождено
                return False
            node = node.left or node.right
        return True

    def _countDepth(self, node: TreeNode) -> int:
        depth = 0
        while node:
            depth += 1
            node = node.left or node.right
        return depth

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if self._isDegenerate(root):
            return self._countDepth(root)
        
        
        # Основной BFS
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return 0
