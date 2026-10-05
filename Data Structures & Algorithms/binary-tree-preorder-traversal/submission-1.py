# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.preorderTraversal_recursive(root, result)
        return result
    
    def preorderTraversal_recursive(self, node, result):
        if node is None:
            return
        
        result.append(node.val)
        self.preorderTraversal_recursive(node.left, result)
        self.preorderTraversal_recursive(node.right, result)
