# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        root = TreeNode(0)  # Временный корень
        stack = [(0, len(nums)-1, root, True)]  # (l, r, parent, is_left)
        
        while stack:
            l, r, parent, is_left = stack.pop()
            if l > r:
                continue
            
            m = l + (r - l) // 2
            node = TreeNode(nums[m])
            
            if is_left:
                parent.left = node
            else:
                parent.right = node
            
            # Добавляем поддиапазоны в стек (порядок: правый, затем левый — для DFS)
            stack.append((m+1, r, node, False))
            stack.append((l, m-1, node, True))
        
        
        return root.left  # Реальный корень — левый потомок временного
