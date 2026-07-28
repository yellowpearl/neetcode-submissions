import heapq

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        for i in range(len(speed)):
            heapq.heappush_max(cars, (position[i], speed[i]))
        
        fleets = 0
        f_s = None
        f_t = None

        while cars:
            car_pos, car_speed = heapq.heappop_max(cars)

            if not f_s:
                f_s = car_speed
                f_t = (target - car_pos) / car_speed
                fleets += 1
            else:
                if (target - car_pos) / car_speed > f_t:
                    f_s = car_speed
                    f_t = (target - car_pos) / car_speed
                    fleets += 1
        
        return fleets