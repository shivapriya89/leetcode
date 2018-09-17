"""class Solution(object):
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
    print(s.sortArrayByParity([1,2,3,4,5,6,7]))"""


class Solution(object):
    def sortArrayByParity(self, A):
        i=0
        j=len(A)-1
        while i < j:
            if A[i]%2==1 and A[j]%2==0:
                A[i],A[j] = A[j],A[i]

            if A[i]%2==0:
                i += 1

            if A[j]%2==1:
                j -= 1
        return A

if __name__=='__main__':
    s=Solution()
    print(s.sortArrayByParity([4,1,2]))