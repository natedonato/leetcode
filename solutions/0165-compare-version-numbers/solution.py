class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        
        v1l = len(version1)
        v2l = len(version2)
        max_l = max(v1l, v2l)

        for i in range(0, max_l):
            if i >= v1l:
                v1= 0
            else:
                v1 = int(version1[i])
            
            if i >= v2l:
                v2= 0
            else:
                v2 = int(version2[i])
            
            if v1 > v2:
                return 1
            elif v2 > v1:
                return -1
        
        return 0
