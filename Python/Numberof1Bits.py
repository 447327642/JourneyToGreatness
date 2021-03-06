class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        cnt = 0
        while n:
            cnt += 1&n
            n >>= 1
        return cnt
