# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return
        elif root and (root.left and root.right):
            root.val = abs(root.left.val-root.right.val)
            self.findTilt(root.left)
            self.findTilt(root.right)
        elif root and (root.left is not None and root.right is None):
            root.val=root.left.val
            self.findTilt(root.left)
        elif root and (root.right is not None and root.left is None):
            root.val=root.right.val
            self.findTilt(root.right)
        elif root and (root.left is None and root.right is None):
            root.val=0
        return root

node=TreeNode(1)
left_node=TreeNode(5)
node.left=left_node
right_node=TreeNode(7)
node.right=right_node

print(Solution().findTilt(node).val)
