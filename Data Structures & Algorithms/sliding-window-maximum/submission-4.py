class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []
        for i in range(k):
            # print(queue)
            if not queue:
                queue.append((nums[i], i))
            else:
                while queue and queue[-1][0] <= nums[i]:
                    queue.pop()
                queue.append((nums[i], i))
                # else:
        result.append(queue[0][0])
        for i in range(k, len(nums)):
            # print(queue)
            if queue[0][1] <= i - k:
                queue.popleft()
            while queue and queue[-1][0] <= nums[i]:
                queue.pop()
            queue.append((nums[i], i))
            result.append(queue[0][0])
        return result

