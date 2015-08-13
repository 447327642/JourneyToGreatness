"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """  
    def isValidBST(self, root):
        # write your code here
        def isValid(root, low, up):
            if not root:
                return True
            if root.val <= low or root.val >= up:
                return False
            return isValid(root.left, low, root.val) \
                and isValid(root.right, root.val, up)
        return isValid(root, -float('inf'), float('inf'))
