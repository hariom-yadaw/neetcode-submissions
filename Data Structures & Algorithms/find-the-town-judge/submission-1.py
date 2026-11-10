class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # There should be at least n - 1 elements in trust
            # - Otherwise "everyone(except) trusts the judge" will not be satishfied
        if len(trust) < n - 1:
            return -1
        
        # Create an array to store the trustScore
        trustScore = [0] * (n + 1) # N + 1 because labels start from 1 to N (not 0)
        for member1, member2 in trust:
            trustScore[member1] -= 1 # decrease for member who trust others
            trustScore[member2] += 1 # Increase for member who gets trusted by others
        
        for i in range(n + 1):
            if trustScore[i] == n - 1: # takes care of [0]
                return i 
        
        return -1 # Town Judge does not exist

        