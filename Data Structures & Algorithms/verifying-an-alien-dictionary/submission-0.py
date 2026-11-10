class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # this is the trick, get the Char to Index dictionary far fast look-up later in loops
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            # Compare each pair of words
            w1, w2 = words[i], words[i+1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    # only first differing character is sufficient to judge the order of w1 and w2
                    break # This is important 
        return True