class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_min = [0 for i in range(len(nums))]
        dp_max = [0 for i in range(len(nums))]
        cur_min = 0
        cur_max = 0
        global_max = float('-inf')
        for i in range(len(nums)):
            if i == 0:
                # dp_min[i] = dp_max[i] = nums[i]
                cur_min = cur_max = nums[i]
            else:
                n = nums[i]
                tmp = cur_max
            
                cur_max = max(n, n * cur_max, n * cur_min)
                cur_min = min(n, n * tmp, n * cur_min)
                # dp_min[i] = min(dp_max[i - 1] * n, n, dp_min[i - 1] * n)
                # dp_max[i] = max(dp_min[i - 1] * n, n, dp_max[i - 1] * n)
            # global_max = max(global_max, dp_max[i])
            global_max = max(global_max, cur_max)
        return global_max