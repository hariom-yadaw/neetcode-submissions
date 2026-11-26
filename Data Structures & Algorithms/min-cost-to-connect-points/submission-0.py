class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        visited = set()
        edgesUsed, totalCost = 0, 0
        node = 0 # Starting point
        INF = float('inf')
        dist = [INF] * N

        while len(visited) < N - 1:
            nextNode = -1
            visited.add(node)

            for i in range(N):
                if i in visited:
                    continue

                curDist = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                dist[i] = min(dist[i], curDist)

                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i

            totalCost += dist[nextNode]
            node = nextNode 

        return totalCost
