class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        count = Counter(tasks)
        for task in count:
            heapq.heappush(heap, (-count[task], task))

        res = 0
        while heap:
            temp = []
            tasks_processed = 0  # Track actual tasks executed in this cycle
            for i in range(n + 1):
                if heap:
                    count, task = heapq.heappop(heap)
                    if -count != 1:
                        temp.append((count + 1, task))
                    tasks_processed += 1  # Successfully processed a task
                    # res += 1
                # if not temp:
                #     return res
                
                # res += 1
            for t in temp:
                heapq.heappush(heap, t)

            # If the heap is empty, it was the final cycle (no trailing idles needed)
            if not heap:
                res += tasks_processed
            # Otherwise, add the full cycle length (tasks + idle time)
            else:
                res += n + 1
        return res