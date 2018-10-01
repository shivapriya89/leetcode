class Solution(object):
    def hammingWeight(self, n):
        nBit=bin(n)[2::]
        count=0
        for x in nBit:
            if x == '1':
                count += 1
        return count

if __name__=='__main__':
    s=Solution()
    print(s.hammingWeight(11))