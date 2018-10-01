class Solution(object):
    def isMonotonic(self, A):
        if sorted(A) == A or sorted(A)[::-1] == A:
            return True
        else:
            return False

if __name__=='__main__':
    s=Solution()
    print(s.isMonotonic([1,3,2]))
    print(s.isMonotonic([1,3,4,5]))
    print(s.isMonotonic([6,5,3]))