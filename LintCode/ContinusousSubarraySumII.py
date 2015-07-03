import unittest
class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the
    #                  first number and the index of the last number
    def continuousSubarraySumII(self, A):
        # Write your code here
        B = A * 2
        res, cur = B[0], 0
        cur_i = 0
        res_i, res_j = 0, 0
        for i in range(len(B)):
            if cur < 0:
                cur = B[i]
                cur_i = i
            else:
                cur += B[i]

            if cur > res:
                res = cur
                res_i, res_j = cur_i, i
        return [res_i, res_j % len(A)]
