class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        i = 0
        l = len(s)
        while i < l:
            count = 0
            current = s[i]
            if i != 0 and s[i] == s[i - 1]:
                i += 1
                continue
            
            while i < l and current == s[i]:
                count += 1
                
                if count == k:
                    if i + 1 >= l or s[i + 1] != current:
                        return True

                i += 1

        return False
            

