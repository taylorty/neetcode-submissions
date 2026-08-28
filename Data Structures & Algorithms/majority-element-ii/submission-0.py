class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
            if m[n] == len(nums) // 3 + 1:
                res.append(n)

        return res