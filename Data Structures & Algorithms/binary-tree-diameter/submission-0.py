# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.treeDiameter = 0
        self.heightOfTree(root)
        return self.treeDiameter

    def heightOfTree(self, root):
        if root is None:
            return 0
        
        leftTreeHeight = self.heightOfTree(root.left)
        rightTreeHeight = self.heightOfTree(root.right)

        diameter = (leftTreeHeight + rightTreeHeight + 1) - 1
        self.treeDiameter = max(self.treeDiameter, diameter)

        return max(leftTreeHeight, rightTreeHeight) + 1