# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.heightAndBalanced(root) != -1

    def heightAndBalanced(self, root):
        if root is None:
            return 0
        
        leftHeightBalance = self.heightAndBalanced(root.left)
        rightHeightBalance = self.heightAndBalanced(root.right)

        if leftHeightBalance == -1 or rightHeightBalance == -1 or \
            abs(leftHeightBalance - rightHeightBalance) > 1:
            return -1

        #balanced = leftHeightBalance[0] and rightHeightBalance[0] and \
        #    abs(leftHeightBalance[1] - rightHeightBalance[1]) <= 1

        return 1 + max(leftHeightBalance, rightHeightBalance)