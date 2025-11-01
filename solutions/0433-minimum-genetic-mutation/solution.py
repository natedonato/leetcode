class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # set of genes in bank
        # queue of current genes
            # get next gene
            # iterate through gene string
                # test if any variation is in the gene bank
                    # add to queue
        #
        b = set(bank)
        seen = set()
        seen.add(startGene)
        q = deque()
        q.append(startGene)
        count = 0

        while q:
            l = len(q)
            for _ in range(l):
                g = q.popleft()
                if g == endGene:
                    return count
                for i in range(len(g)):
                    for c in "ACGT":
                        next_gene = g[:i] + c + g[i+1:]
                        if next_gene not in seen and next_gene in b:
                            seen.add(next_gene)
                            q.append(next_gene)
            
            count += 1

        return -1
