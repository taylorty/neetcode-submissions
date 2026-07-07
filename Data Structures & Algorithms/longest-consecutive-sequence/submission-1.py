class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        s = set(nums)
        maxLen = 0

        for i in range(n):
            num = nums[i]
            curr_len = 1

            if num - 1 not in s:
                # s.remove(num)
                # before = num - 1
                # while before in s:
                #     curr_len += 1
                #     s.remove(before)
                #     before -= 1
                after = num + 1
                while after in s:
                    curr_len += 1
                    s.remove(after)
                    after += 1
                    
            
            maxLen = max(maxLen, curr_len)

        return maxLen