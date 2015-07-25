class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        """ binary search to find the suitable length
        Args:
            L: list of wood
            k: integer of required # of pieces
        Returns:
            res: result
        """
        if sum(L) < k:
            return 0
        # bsearch find possible length
        res = -1
        left, right = 1, max(L)
        while left <= right:
            mid = left + (right - left) / 2
            n_pieces = sum([l / mid for l in L])
            if n_pieces >= k:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        if res == -1:
            return 0
        return res
