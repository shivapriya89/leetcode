class Solution(object):
    def maxCount(self, m, n,ops):
        if not ops:
            return m*n
        return min(op[0] for op in ops)*min(op[1] for op in ops)

if __name__=='__main__':
    s=Solution()
    print(s.maxCount(3,3,[[2,2],[3,3]]))