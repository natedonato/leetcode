class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swapped = False
        seen1 = ""
        seen2 = ""
        for i in range(0,len(s1)):
            c1 = s1[i]
            c2 = s2[i]
            
            if c1 != c2:
                if swapped == True:
                    return False
                
                if seen1 == "":
                    seen1 = c1
                    seen2 = c2
                else:
                    if c2 == seen1 and c1 == seen2:
                        swapped = True
                    else: 
                        return False
                    
        
        return swapped or seen1 == seen2
            
