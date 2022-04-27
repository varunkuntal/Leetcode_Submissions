# Problem URL: https://leetcode.com/problems/path-crossing/submissions/

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pathnum = [[0,0]]
        d = {}
        n = len(path)
        d[str(pathnum[0])] = 1
        for i in range(1, n+1):
            if path[i-1] == 'N':
                pathnum.append([pathnum[i-1][0], pathnum[i-1][1]+1])
            elif path[i-1] == 'S':
                pathnum.append([pathnum[i-1][0], pathnum[i-1][1]-1])
            elif path[i-1] == 'E':
                pathnum.append([pathnum[i-1][0]+1, pathnum[i-1][1]])
            elif path[i-1] == 'W':
                pathnum.append([pathnum[i-1][0]-1, pathnum[i-1][1]])
                
            if d.get(str(pathnum[i])):
                return True
            else:
                d[str(pathnum[i])] = 1
            
        return False