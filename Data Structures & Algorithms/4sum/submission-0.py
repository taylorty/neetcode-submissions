class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        i = 0
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            threeSumResults = self.threeSum(nums[i + 1:], target - nums[i])
            for triplet in threeSumResults:
                result.append([nums[i]] + triplet)
        return result

    
    def threeSum(self, nums, target):
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
                elif nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        return res

