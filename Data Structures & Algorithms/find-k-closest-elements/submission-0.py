class Solution:
    def findClosestElements(self, nums: List[int], k: int, target: int) -> List[int]:
        # Binary search for the starting point of the k-length window
        left, right = 0, len(nums) - k
        
        while left < right:
            mid = (left + right) // 2
            # Compare the distance of the element just before the window 
            # and the element at the end of the window
            if target - nums[mid] > nums[mid + k] - target:
                left = mid + 1
            else:
                right = mid
                
        return nums[left : left + k]