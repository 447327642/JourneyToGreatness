# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)


def show(stack):
    print '[',
    for s in stack:
        print s,
    print ']',
    
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        cnt = 0
        p = root
        while stack or p:

            if p != None:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                cnt += 1
                if cnt == k:
                    return p.val
                p = p.right

        return 0


so = Solution()

n2 = TreeNode(2, TreeNode(1), TreeNode(3))
n6 = TreeNode(6, TreeNode(5), TreeNode(7))
root = TreeNode(4, n2, n6)
print so.kthSmallest(root, 7)
