# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if not root:
            return res
        def dfs(node, buff, res):
            if not node.left and not node.right:
                buff.append(str(node.val))
                res.append('->'.join(buff))
                buff.pop()
                return
            buff.append(str(node.val))
            if node.left:
                dfs(node.left, buff, res)
            if node.right:
                dfs(node.right, buff, res)
            buff.pop()
        dfs(root, [], res)
        return res
