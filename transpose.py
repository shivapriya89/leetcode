class Solution(object):
    def transpose(self,A):
        #return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
        res = []
        for j in range(len(A[0])):
            res.append([])
            for i in range(len(A)):
                res[j].append(A[i][j])
        return res

if __name__=='__main__':
    s=Solution()
    #print (s.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9],[10,11,12]]))
    #print(s.transpose([[1],[2],[3]]))
    print(s.transpose([[1,2],[3,4]]))
    #print(s.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))