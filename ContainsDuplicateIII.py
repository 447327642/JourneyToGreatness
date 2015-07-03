class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        ind = sorted(range(len(nums)), key = lambda i: nums[i])
        for i in range(len(nums) - 1):
            j = i + 1
            while j < len(nums) and abs(nums[ind[j]] - nums[ind[i]]) <= t:
                if abs(ind[j] - ind[i]) <= k:
                    return True
                j += 1
        return False
