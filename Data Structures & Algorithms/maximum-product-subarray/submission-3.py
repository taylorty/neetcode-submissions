class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_min = [0 for i in range(len(nums))]
        dp_max = [0 for i in range(len(nums))]
        min_so_far = 0
        max_so_far = 0
        global_max = float('-inf')
        for i in range(len(nums)):
            if i == 0:
                dp_min[i] = dp_max[i] = nums[i]
            else:
                dp_min[i] = min(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])
                dp_max[i] = max(dp_min[i - 1] * nums[i], nums[i], dp_max[i - 1] * nums[i])
            global_max = max(global_max, dp_max[i], dp_min[i])
        return global_max