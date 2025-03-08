class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_block_count = 0
        minimum_count = k
        l = len(blocks)
        for i in range(0, l):
            # block entering our run of K
            if blocks[i] == "W":
                white_block_count += 1
            
            #block behind our run of K
            if i >= k:
                if blocks[i - k] == "W":
                    white_block_count -= 1

            if i >= k - 1:  
                minimum_count = min(minimum_count, white_block_count)

        return minimum_count


