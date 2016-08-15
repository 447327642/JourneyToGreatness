# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return
        tmp = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(tmp)
        return root
