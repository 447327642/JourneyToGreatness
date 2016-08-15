class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if len(nums) == 0:
            return 0
        start, end = 0, 0
        best = len(nums) + 1
        cur_sum = 0
        while end < len(nums):
            while end < len(nums) and cur_sum < s:
                cur_sum += nums[end]
                end += 1
            while cur_sum >= s:
                best = min(best, end - start)
                cur_sum -= nums[start]
                start += 1
        return best if best <= len(nums) else 0
