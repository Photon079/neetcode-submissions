class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # 1. Create pairs of (position, speed) and sort them in descending order
        # based on position (closest to target first).
        # zip(position, speed) creates tuples like (10, 2), (8, 4), etc.
        # sorted(..., reverse=True) sorts them from largest position to smallest.
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        slowest_time = 0.0  # We use a float because time can be a fraction
        
        # 2. Iterate through each car from the closest to the target to the furthest
        for pos, spd in cars:
            # Calculate time to reach the target
            # Formula: Distance / Speed
            time = (target - pos) / spd
            
            # 3. If this car takes LONGER than the slowest car ahead of it,
            # it cannot catch up. It forms a new fleet.
            if time > slowest_time:
                fleets += 1
                # Update the slowest time to this new, slower fleet
                slowest_time = time
            
            # If time <= slowest_time, it catches the fleet ahead. 
            # We do nothing, it just joins the existing fleet.
            
        return fleets