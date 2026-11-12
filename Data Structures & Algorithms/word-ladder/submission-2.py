from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        
        if endWord not in wordSet or beginWord == endWord:
            return 0
        
        queue = deque()
        visited = set()

        queue.append((beginWord, 1)) # start with begin word with 1 transformation
        
        while queue:
            currentWord, transformations = queue.popleft()
            if currentWord == endWord:
                return transformations
            
            for i in range(len(currentWord)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c != currentWord[i]:
                        nextWord = currentWord[:i] + c + currentWord[i + 1:]
                        if nextWord in wordSet and nextWord not in visited:
                            queue.append((nextWord, transformations + 1))
                            visited.add(nextWord)

        return 0 