# Problem URL: https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        store_index = {}

        for index in range(len(order)):

            store_index[order[index]] = index


        for i in range(len(words)-1):

            for j in range(len(words[i])):

                if j >= len(words[i+1]):
                    return False

                elif words[i][j] != words[i+1][j]:

                    if store_index[words[i][j]] > store_index[words[i+1][j]]:

                        return False
                    else:
                        break

        return True
        
        
        
        