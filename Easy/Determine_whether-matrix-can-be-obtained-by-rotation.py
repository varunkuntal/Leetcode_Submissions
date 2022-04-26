https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/submissions/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        n = len(mat)
        
        Bool = [False, False, False]
                
        if mat == target:
            return True
          
        # 90 degrees to the right
        for i in range(n):
            for j in range(n-1, -1, -1):
                if mat[j][i] != target[i][n-1-j]:
                    Bool[0] = False
                    
        if Bool[0]:
            return True
                    
        # 90 degrees to the left
        for i in range(n-1, -1, -1):
            for j in range(n):
                if mat[j][i] != target[n-1-i][j]:
                    Bool[1] = False
                    
        if Bool[1]:
            return True
        
        # 180 degrees
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if mat[i][j] != target[n-1-i][n-1-j]:
                    Bool[2] = False
                    
        if Bool[2]:
            return True