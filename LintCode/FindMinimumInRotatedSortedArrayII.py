class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        res = float('inf')
        left, right = 0, len(num) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if num[left] < num[mid]:
                res = min(res, num[left])
                left = mid + 1
            elif num[mid] < num[right]:
                res = min(res, num[mid])
                right = mid - 1
            else: # num[left] >= num[mid] and num[mid] >= num[right] and at most 1 >
                res = min(res, num[left])
                left += 1
        return res
