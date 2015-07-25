"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        # write your code here
        def build(start, end):
            res = []
            if start > end:
                res.append(None)
                return res
            for r in xrange(start, end + 1):
                ltree = build(start, r - 1)
                rtree = build(r + 1, end)
                for i in ltree:
                    for j in rtree:
                        root = TreeNode(r)
                        root.left = i
                        root.right = j
                        res.append(root)
            return res
            
        return build(1, n)
