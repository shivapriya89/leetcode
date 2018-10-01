class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def mergeTrees(self, t1, t2):
        if t1 and t2:
            t1 += t2
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        else:
            return t1 or t2

