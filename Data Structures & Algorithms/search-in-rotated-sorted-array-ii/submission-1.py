class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        while s <= e:
            m = (e - s) // 2 + s
            if target == nums[m]:
                return True
            if nums[s] <= nums[m]: # left is sorted
                if nums[s] <= target < nums[m]:
                    e -= 1
                else:
                    s += 1
            else:
                if nums[m] < target <= nums[e]:
                    s += 1
                else:
                    e -= 1
        return False