from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        INF = float('inf')
        delay = [INF] * (n + 1)
        delay[k] = 0
    
        pq = []
        heapq.heappush(pq, (0, k)) # push start node with zero distnace

        while pq:
            time, node = heapq.heappop(pq) # the the node with min distance

            if time > delay[node]: # stale entry
                continue
            
            for neighbor, t in graph[node]:
                if time + t < delay[neighbor]:
                    delay[neighbor] = time + t
                    heapq.heappush(pq, (time + t, neighbor))
        
        maxDelay = max(delay[1:]) # ignore 0-index
        return maxDelay if maxDelay != INF else - 1
        

        