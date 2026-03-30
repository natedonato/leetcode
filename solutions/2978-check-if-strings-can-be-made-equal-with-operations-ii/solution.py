class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:

        if len(s1) != len(s2):
            return False

        e1 = ""
        e2 = ""
        o1 = ""
        o2 = ""

        for i in range(len(s1)):
            if i % 2 == 0:
                e1 += s1[i]
                e2 += s2[i]
            else:
                o1 += s1[i]
                o2 += s2[i]

        e1 = "".join(sorted(e1))
        e2 = "".join(sorted(e2))
        o1 = "".join(sorted(o1))
        o2 = "".join(sorted(o2))

        return (e1 == e2) and (o1 == o2)
