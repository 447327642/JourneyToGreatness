# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)

def show(stack, p):
    print '[',
    for i in stack:
        print i,
    print ']',
    print p,
    
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack, res = [], []
        p = root
        while stack or p != None:
            show(stack, p)
            if p != None:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                print p,
                res.append(p.val)
                p = p.right
            print
        return res
    
so = Solution()

n2 = TreeNode(2, TreeNode(1), TreeNode(3))
n6 = TreeNode(6, TreeNode(5), TreeNode(7))
root = TreeNode(4, n2, n6)

print so.inorderTraversal(root)
