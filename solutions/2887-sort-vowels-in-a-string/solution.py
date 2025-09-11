class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        vowel_str = "AEIOUaeiou"
        idxes = deque()
        for i, c in enumerate(s):
            if c in vowel_str:
                vowels.append(c) 
                idxes.append(i)

        vowels.sort(key=lambda v: -ord(v))
    
        out = []
        for i in range(len(s)):
            if idxes and idxes[0] == i:
                out.append(vowels.pop())
                idxes.popleft()
            else:
                out.append(s[i])

        return "".join(out)
