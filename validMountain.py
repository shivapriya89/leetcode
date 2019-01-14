class Solution(object):
    def validMountainArray(self, A):
        if len(A) < 3:
            return False
        peak1=A[0]
        peak2=A[-1]
        i=0
        j=len(A)-1
        while i < len(A):
            if A[i+1] > A[i]:
                peak1=A[i+1]
                i += 1
                if peak1 == A[-1] and i == len(A)-1:
                    return False
                else:
                    continue
            if A[i+1] <= A[i]:
                break

        while j > -1:
            if A[j] < A[j-1]:
                peak2=A[j-1]
                j -= 1
                if peak2 == A[0] and j == 0:
                    return False
                else:
                    continue
            if A[j] >= A[j-1]:
                break

        if peak1==peak2 and i==j:
            return True
        else:
            return False

if __name__=='__main__':
    s=Solution()
    print(s.validMountainArray([0,1,2,3,2,4]))