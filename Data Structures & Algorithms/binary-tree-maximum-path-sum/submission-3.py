# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0) # To ignore -ve values, they donlt contribute 
            rightMax = max(rightMax, 0) # To ignore -ve values

            # at a node, calculate two values
            # 1. Max Path through the node if allowed to split
            res[0] = max(res[0], root.val + leftMax + rightMax) 
            # 2. If not allowed to split, what value to return for its parent ?
                # node' value + max of (left, right)
            return root.val + max(leftMax, rightMax) # Return value for this fucntion is different
        
        dfs(root)
        return res[0]