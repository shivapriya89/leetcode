class Solution(object):
    def isPowerOfTwo(self, n):
        if n < 0:
            return False
        if n == 1:
            return True
        if n == 2:
            return True
        if n == 0:
            return False
        if n%2 != 0:
            return False
        while n>2:
            """while n/2 != 1:
                n= int(n/2)
                if n%2!=0:
                    return False
                if n/2==1.0:
                    return True"""
            if n % 2 != 0:
                return False
            n = n /2
        return True

if __name__=='__main__':
    s=Solution()
    print(s.isPowerOfTwo(6))
    print(s.isPowerOfTwo(8))
    print(s.isPowerOfTwo(7))