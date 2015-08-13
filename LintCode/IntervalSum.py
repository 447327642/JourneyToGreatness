"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution: 
    """
    @param A, queries: Given an integer array and an Interval list
                       The ith query is [queries[i-1].start, queries[i-1].end]
    @return: The result list
    """
    def intervalSum(self, A, queries):
        # write your code here
        prefix = [0] * (len(A) + 1)
        
        for i in range(len(A)):
            prefix[i+1] = prefix[i] + A[i]
        res = []
        for q in queries:
            start, end = q.start, q.end
            res.append(prefix[end+1] - prefix[start])
        return res
