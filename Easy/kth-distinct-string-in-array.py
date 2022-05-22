class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        c = 0
        d = {}
        for i in arr:
            if d.get(i):
                d[i] += 1
            else:
                d[i] = 1

        l = list(d.keys())[:]
        for i in l:
            if d.get(i) and d[i] > 1:
                del(d[i])
                
        if k > len(d):
            return ""
                
        for i,j in enumerate(d.keys()):
            if i == k-1:
                return j if j else ""
            