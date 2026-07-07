from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # Map each stop to the buses (by index) that stop there
        stop_to_buses = defaultdict(list)
        for bus_id, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_id)
                
        # Queue stores: (current_stop, number_of_buses_taken)
        queue = deque([(source, 0)])
        
        # Track visited stops and buses to prevent cycles and redundant work
        visited_stops = {source}
        visited_buses = set()
        
        while queue:
            current_stop, bus_count = queue.popleft()
            
            # Check all buses that visit the current stop
            for bus_id in stop_to_buses[current_stop]:
                if bus_id not in visited_buses:
                    visited_buses.add(bus_id)
                    
                    # Check all stops this newly boarded bus visits
                    for next_stop in routes[bus_id]:
                        if next_stop not in visited_stops:
                            if next_stop == target:
                                return bus_count + 1
                            
                            visited_stops.add(next_stop)
                            queue.append((next_stop, bus_count + 1))
                            
        return -1