# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesDFS(root, root.val)
    
    def goodNodesDFS(self, node, maxValInPath):
        if not node:
            return 0
        
        res = 0

        if node.val >= maxValInPath:
            maxValInPath = node.val
            res = 1
        else:
            res = 0
        
        leftCount = self.goodNodesDFS(node.left, maxValInPath)
        rightCount = self.goodNodesDFS(node.right, maxValInPath)

        return res + leftCount + rightCount
