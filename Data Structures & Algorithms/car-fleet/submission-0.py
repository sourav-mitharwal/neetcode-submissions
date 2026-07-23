class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed))
        fleet = 0
        last_time = 0
        for p,s in reversed(cars):
            time = (target-p) / s
            if time > last_time:
                fleet += 1
                last_time = time
        return fleet