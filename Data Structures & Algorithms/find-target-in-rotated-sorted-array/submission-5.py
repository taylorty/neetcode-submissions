class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        while s <= e:
            m = (e - s) // 2 + s
            if nums[m] == target:
                return m
            # 1. Check if the LEFT half is sorted
            if nums[s] <= nums[m]:
                # Is the target within this left sorted half?
                if nums[s] <= target < nums[m]:
                    e = m - 1
                else:
                    s = m + 1
                    
            # 2. Otherwise, the RIGHT half must be sorted
            else:
                # Is the target within this right sorted half?
                if nums[m] < target <= nums[e]:
                    s = m + 1
                else:
                    e = m - 1

        return -1
