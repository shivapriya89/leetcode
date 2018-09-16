class Solution(object):
    def flipAndInvertImage(self, A):
        res = []
        for i in A:
            res.append([0 if x == 1 else 1 for x in i][::-1])
        return res


if __name__=='__main__':
    s=Solution()
    print(s.flipAndInvertImage([[0,1],[1,0]]))
    #print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))