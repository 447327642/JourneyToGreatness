class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if x <= 0:
            return 0
        res = -1
        # why x? if x == 1, we cannot use x/2
        left, right = 1,  x
        while left <= right:
            mid = left + (right - left) / 2
            # in this case, we need to find lower bound
            if mid * mid <= x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
