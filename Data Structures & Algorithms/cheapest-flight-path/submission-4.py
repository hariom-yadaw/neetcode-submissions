from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # K stops means, K intermediate cities. so the path has at-most k+1 edges
        # Bell-man ford over K+1 loops, not all V-1
            # Effectively relax each edge K+1 times, not V-1 times

        INF = float('inf')
        prices = [INF] * n
        prices[src] = 0

        for _ in range(k+1): # at most k+1 edges
            # Temporary copy for each edge loop round
            tmpPrices = prices.copy()

            for source, destination, cost in flights:
                if prices[source] != INF and prices[source] + cost < tmpPrices[destination]:
                    tmpPrices[destination] = prices[source] + cost

            prices = tmpPrices

        return prices[dst] if prices[dst] != INF else -1
            
