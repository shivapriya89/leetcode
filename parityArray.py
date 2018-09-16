class Solution(object):
    def sortArrayByParity(self, A):
        even=[]
        odd=[]
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            if A[i] % 2 != 0:
                odd.append(A[i])
        return even+odd

if __name__=='__main__':
    s=Solution()
    print(s.sortArrayByParity([1,2,3,4,5,6,7]))
