class Solution(object):
    def peakIndexInMountainArray(self, A):
        index=0
        if len(A) < 3:
            return False
        for i in range(1,len(A)-1):
            if A[index] < A[i]:
                index += 1
        return index

if __name__=='__main__':
    s=Solution()
    print(s.peakIndexInMountainArray([0,1,2,3,1,0]))