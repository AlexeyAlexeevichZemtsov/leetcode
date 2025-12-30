class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return []
            
        # stack = [root]
        # res = []
        
        # while stack:
        #     # Достаём текущий узел из стека
        #     node = stack.pop()
        #     res.append(node.val)
            
        #     # Добавляем правого потомка первым (чтобы левый обработался раньше)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
                
        # return res
        if not root:
            return []
        return ([root.val] + 
                self.preorderTraversal(root.left) +
                self.preorderTraversal(root.right))
