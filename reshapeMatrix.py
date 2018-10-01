class Solution(object):
    def matrixReshape(self, nums, r, c):
        row=len(nums)
        col=len(nums[0])
        l=[]
        for i in range(row):
            for j in range(col):
                l.append(nums[i][j])

        elements = len(l)
        if r*c != elements:
            return nums

        res=[]
        x=0
        for j in range(r):
            res.append([])
            for i in range(c):
                res[j].append(l[x])
                x+=1
        return res

if __name__=='__main__':
    s=Solution()
    print(s.matrixReshape([[1,2],[3,4]],4,1))
    print(s.matrixReshape([[1,2],[3,4]],1,4))