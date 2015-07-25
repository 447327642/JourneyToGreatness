ass Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.

    # O(n)
    def findPeak(self, A):
        # write your code here
        for i in range(len(A)):
            if i > 0 and A[i] < A[i-1]:
                continue
            if i < len(A) - 1 and A[i] < A[i+1]:
                continue
            return i

    # O(LogN)
    def findPeak2(self, A):
        # write your code here
        res = -1
        left, right = 0, len(A) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if mid > 0 and A[mid] < A[mid - 1]:
                right = mid - 1
            elif mid < len(A) - 1 and A[mid] < A[mid + 1]:
                left = mid + 1
            else:
                return mid
        if A[left] > A[right]:
            return left
        else:
            return right
