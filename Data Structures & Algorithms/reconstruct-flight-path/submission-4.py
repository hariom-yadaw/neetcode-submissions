from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]: # reverse sorted
            graph[src].append(dst)
        
        res = []
        def dfs(src):
            while graph[src]:
                dst = graph[src].pop()
                dfs(dst)
            res.append(src)
        
        dfs('JFK')
        return res[::-1] 
        # Time Complexity: O(E*logE)
        # Space Complexity: O(E)
         

    def findItinerary_DFS(self, tickets: List[List[str]]) -> List[str]:
        # This is DFS based Solution
        graph = defaultdict(list)
        tickets.sort() # it will sort the edges (src, dest) -> for a src, all destinations will be sorted
        for src, dest in tickets:
            graph[src].append(dest)
        
        if 'JFK' not in graph:
            return []
        
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in graph: # if airport doesn't have any outgoing destination
                return False
            
            temp = list(graph[src]) # You can't iterate and modify the list at same time, hence temp
            for i, v in enumerate(temp):
                graph[src].pop(i) # remove it from graph
                res.append(v) # add it to result

                if dfs(v):
                    return True
                
                # Backtracking if DFS(v) above fails because of no outgoing destination from airport v
                graph[src].insert(i, v) # add it back to graph
                res.pop() # remove from result
            return False

        dfs("JFK")        
        return res

        # Time Complexity: O(E * V)
        # Space Complexity: O(E * V)