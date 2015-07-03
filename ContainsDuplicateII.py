class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        from collections import defaultdict
        mark = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] not in mark:
                mark[nums[i]] = i
            else:
                if i - mark[nums[i]] <= k:
                    return True
                mark[nums[i]] = i
        return False
                    
