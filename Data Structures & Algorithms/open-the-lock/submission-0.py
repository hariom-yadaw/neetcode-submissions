from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        if target == '0000':
            return 0

        deadEndSet = set(deadends)
        visited = set()

        queue = deque()
        queue.append(("0000", 0)) # initial state, rotation count
        visited.add("0000")

        # BFS Traversal
        while queue:
            lock, numTurns = queue.popleft()

            if lock == target:
                return numTurns
            
            for child in self.children(lock):
                if child not in visited and child not in deadEndSet:
                    queue.append((child, numTurns + 1))
                    visited.add(child)
        
        return -1
    
    def children(self, lock):
        res = []

        for i in range(4):
            # +1 for forward wheel turn
            digit = str((int(lock[i]) + 1) % 10)
            res.append(lock[:i] + digit + lock[i+1:])
            # -1 for reverse wheel turn
            digit = str((int(lock[i]) - 1) % 10)
            res.append(lock[:i] + digit + lock[i+1:])

        return res

