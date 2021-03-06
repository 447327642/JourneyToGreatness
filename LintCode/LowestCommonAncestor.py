"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if not root:
            return None
        if root.val == A.val or root.val == B.val:
            return root
        L = self.lowestCommonAncestor(root.left, A, B)
        R = self.lowestCommonAncestor(root.right, A, B)
        if L and R:
            return root
        return L if L else R
            
