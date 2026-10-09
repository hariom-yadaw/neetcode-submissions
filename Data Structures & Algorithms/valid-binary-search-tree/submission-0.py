# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidDFS(root, float("-inf"), float("inf"))
    
    def isValidDFS(self, node, minVal, maxVal):
        if not node:
            return True
        
        if not(minVal < node.val < maxVal):
            return False
        
        return self.isValidDFS(node.left, minVal, node.val) and \
                self.isValidDFS(node.right, node.val, maxVal)
