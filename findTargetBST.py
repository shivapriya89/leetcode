import collections

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        if not root:
            return False
        s = set()
        q = collections.deque([root])
        while q:
            n = q.popleft()
            if n:
                if k - n.val in s:
                    return True
                s.add(n.val)
                q.append(n.left)
                q.append(n.right)
        return False

node=TreeNode(3)
left=TreeNode(2)
node.left=node.left
right=TreeNode(4)
node.right=node.right
print(Solution().findTarget(node,5))