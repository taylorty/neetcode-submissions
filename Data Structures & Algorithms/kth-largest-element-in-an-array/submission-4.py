class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        target = len(nums) - k
        def partition(left, right):
            p = right
            store = left
            for i in range(left, right):
                if nums[i] <= nums[p]:
                    nums[i], nums[store] = nums[store], nums[i]
                    store += 1
            nums[p], nums[store] = nums[store], nums[p]
            return store

            
        while left <= right:
            p = partition(left, right)
            if p == target:
                return nums[p]
            elif target > p:
                left = p + 1
            else:
                right = p - 1
        return left

        