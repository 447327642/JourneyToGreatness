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
    @return: An integer
    """ 
    def minDepth(self, root):
        # write your code here
        if root == None:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


    def minDepth2(self, root):
        # write your code here
        if not root:
            return 0
        from collections import deque
        queue = deque([(root, 1)])
        while queue:
            node, dep = queue.popleft()
            if not node.left and not node.right:
                return dep
            if node.left:
                queue.append((node.left, dep+1))
            if node.right:
                queue.append((node.right, dep+1))
        # will never reach here
        return 0
        
        
