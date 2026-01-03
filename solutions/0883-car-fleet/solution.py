class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()
        stack = []

        for car in cars:
            position, speed = car
            dist_to_target = target - position
            time_at_target = dist_to_target / speed

            while stack and time_at_target >= stack[-1]:
                stack.pop()

            stack.append(time_at_target)

        return len(stack)
