# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = deque()
        queue2 = deque()

        queue1.append(p)
        queue2.append(q)

        while queue1 or queue2:
            for _ in range(len(queue1)):
                nodeP = queue1.popleft()
                nodeQ = queue2.popleft()

                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False
                
                #push childtren without cheking if they are null, null get caught in above condition
                queue1.append(nodeP.left)
                queue1.append(nodeP.right)

                #push childtren without cheking if they are null, null get caught in above condition
                queue2.append(nodeQ.left)
                queue2.append(nodeQ.right)
        
        return True
