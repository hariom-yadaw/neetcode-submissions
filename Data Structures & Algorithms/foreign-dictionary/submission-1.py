class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Initialize the graph
        inDegree = {}
        graph = {}
        for word in words:
            for char in word:
                inDegree[char] = 0
                graph[char] = []

        # Build the graph, edges are not given (derive edges from words list first)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            foundDifference = False
            for j in range(min(len(w1), len(w2))):
                parent, child = w1[j], w2[j]
                if w1[j] != w2[j]: # W1 comes first and then w2 in alien dictionary
                    graph[parent].append(child)
                    inDegree[child] += 1
                    foundDifference = True
                    break # Only first different character will help us find the order

            # a word can not come before its own prefixes: 'abc' before 'ab' is not a valid dictionary
            if not foundDifference and len(w1) > len(w2):
                return ""
        
        # find all sources
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        # Dequeue and put the insert ready sources in queue
        sortedOrder = []
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)

            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        if len(sortedOrder) != len(inDegree):
            return ""
        
        return ''.join(sortedOrder)
