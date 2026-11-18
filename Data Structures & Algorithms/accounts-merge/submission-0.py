class UnionFindBySize:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size
    
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
        return True

from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        numAcc = len(accounts)
        uf = UnionFindBySize(numAcc)

        emailToAccIndex = {} # Maps each email to account Index

        for i, account in enumerate(accounts):
            for email in account[1:]: # account[0] = name
            # Email can be in ma via some other accounts
                if email in emailToAccIndex:
                    uf.union(i, emailToAccIndex[email]) # Union current account and previous account
                else:
                    emailToAccIndex[email] = i # assign the index
        
        emailGroup = defaultdict(list)

        for email, index in emailToAccIndex.items():
            leader = uf.find(index)
            emailGroup[leader].append(email)
        
        result = []

        for rootIndex, emails in emailGroup.items():
            name = accounts[rootIndex][0]
            result.append([name] + sorted(emails)) # Array concatenation
        
        return result