# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorderTraversal_Recursive(root, result)
        return result
    
    def inorderTraversal_Recursive(self, Node, result):
        if Node is None:
            return

        self.inorderTraversal_Recursive(Node.left, result)
        result.append(Node.val)
        self.inorderTraversal_Recursive(Node.right, result)
    
