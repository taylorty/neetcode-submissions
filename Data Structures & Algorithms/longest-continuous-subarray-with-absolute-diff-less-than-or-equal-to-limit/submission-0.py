class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_so_far = nums[0]
        max_so_far = nums[0]
        # i = 0
        # j = 0
        length = 0
        for i in range(len(nums)):
            min_so_far = nums[i]
            max_so_far = nums[i]
            j = i
            while j < len(nums):
                min_so_far = min(min_so_far, nums[j])
                max_so_far = max(max_so_far, nums[j])
                
                if abs(min_so_far - max_so_far) <= limit:
                    length = max(length, j - i + 1)
                else:
                    break
                j += 1
        return length