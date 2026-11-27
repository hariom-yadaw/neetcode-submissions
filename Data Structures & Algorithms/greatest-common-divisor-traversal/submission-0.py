class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * (n)
        self.connectedComp = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)

        if rootX == rootY:
            return False

        if self.size[rootX] < self.size[rootY]:
            rootX, rootY = rootY, rootX

        self.parent[rootY] = rootX
        self.size[rootX] += self.size[rootY]
        self.connectedComp -= 1
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))

        factorIndex = {} # To store the index of numbers with factor f
        for i, num in enumerate(nums):
            f = 2
            while f * f <= num:
                if num % f == 0: # f is a prime factor
                    if f in factorIndex:
                        uf.union(i, factorIndex[f])
                    else:
                        factorIndex[f] = i

                    while num % f == 0: # renove all dupliecate prime factor like 2*2*3*5 = 60
                        num = num // f # Integer Division
                
                f += 1 # Increase f
            
            if num > 1: # num is the one last reamining prime factor
                if num in factorIndex:
                    uf.union(i, factorIndex[num])
                else:
                    factorIndex[num] = i
        
        return uf.connectedComp == 1
