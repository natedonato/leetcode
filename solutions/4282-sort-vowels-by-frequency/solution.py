class Solution:
    def sortVowels(self, s: str) -> str:
        vs = ['a', 'e', 'i', 'o', 'u']
        counts = collections.Counter(s)

        first_idx = {}

        for i, c in enumerate(s):
            if c not in first_idx:
                first_idx[c] = i
        
        vs.sort(key=lambda x: (-counts[x], first_idx[x] if x in first_idx else math.inf))
        vowels = set(vs)

        out = []

        for c in s:
            if c in vowels:
                out.append(vs[0])
                counts[vs[0]] -= 1
                if counts[vs[0]] == 0:
                    vs = vs[1:]
            else:
                out.append(c)
        
        return "".join(out)
