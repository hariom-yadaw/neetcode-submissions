"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Create a dictionary for Old Node to Cloned Node
        oldToNew = {}

        if not node: # return null if node is null
            return node

        def clone_dfs(node):
            # first check in the dictionary if copy is already available ?
            if node in oldToNew:
                return oldToNew[node]
            
            # If not available, create a copy of node
            copy = Node(node.val)
            oldToNew[node] = copy # put this into dictionary

            # for all neighbors of node, do the same
            for neighbor in node.neighbors:
                copy.neighbors.append(clone_dfs(neighbor))
            
            return copy # return copy
        
        return clone_dfs(node)