"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Time:  O(mn)
# Space: O(h)
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        # write your code here
        if T2 is None:
            return True
        elif T1 is None:
            return False
        else:
            return self.isSameTree(T1, T2) or self.isSubtree(T1.left, T2) \
                or self.isSubtree(T1.right, T2)
                
    def isSameTree(self, T1, T2):
        if T1 is None and T2 is None:
            return True
        if T1 and T2:
            return T1.val == T2.val and self.isSameTree(T1.left, T2.left) \
                and self.isSameTree(T1.right, T2.right)
        return False
                
