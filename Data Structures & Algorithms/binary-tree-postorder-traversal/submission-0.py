# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.postorderTraversal_recursive(root, result)
        return result
    
    def postorderTraversal_recursive(self, node, result):
        if node is None:
            return
        
        self.postorderTraversal_recursive(node.left, result)
        self.postorderTraversal_recursive(node.right, result)
        result.append(node.val)