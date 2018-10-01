class Solution(object):
    def hasAlternatingBits(self, n):
        nBit=bin(n)[2::]
        if '11' in nBit or '00' in nBit:
            return False
        else:
            return True

if __name__=='__main__':
    s=Solution()
    print(s.hasAlternatingBits(6))
    print(s.hasAlternatingBits(5))
