class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(numbers):
            
            if target - num in m:
                return [m[target - num] + 1, i + 1]
            m[num] = i
        return -1