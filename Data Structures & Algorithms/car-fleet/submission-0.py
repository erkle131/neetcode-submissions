class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for pos, speed in zip(position, speed):
            cars.append((pos, speed))
        cars.sort()

        stack = []
        
        # Use time to reach target: (target - pos) / speed
        last_pos, last_speed = cars[-1]
        last_time = (target - last_pos) / last_speed
        stack.append(last_time)

        for i in range(len(cars) - 2, -1, -1):
            cur_pos, cur_speed = cars[i]
            cur_time = (target - cur_pos) / cur_speed
            # If current car takes more time than the fleet in front, it starts a new fleet
            if cur_time > stack[-1]:
                stack.append(cur_time)

        return len(stack)