class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        current_height = heights[0]
        current_index = 0
        queue = []
        n = len(heights)

        while current_index < n -1:
            next_height = heights[current_index + 1]

            if next_height <= current_height:
                current_height = next_height
                current_index += 1
                continue

            height_difference = next_height - current_height
            heapq.heappush(queue, -height_difference)
            bricks -= height_difference
            while(bricks < 0 and ladders > 0):
                ladders -= 1
                bricks += -heapq.heappop(queue)

            if(bricks < 0):
                return current_index
            else:
                current_height = next_height
                current_index += 1

        return current_index
