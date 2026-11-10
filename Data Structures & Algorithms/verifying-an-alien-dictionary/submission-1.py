class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create Char to index dictionary
            # - This is important for faster look-up later 
                # in words comparison later character by character
        orderIndex = {c : i for i, c in enumerate(order) }

        # compare each pair of words, one-by-one
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # Assume W1 has more characters than W2; means len(w1) > len(w2)
                # if len(w1) <= len(w2) => only we need to check 1st differing character
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if orderIndex[w1[j]] > orderIndex[w2[j]]:
                        return False
                    # 1st differing character is suffiecint to check order for W1, W2
                    break # This is important
        
        return True