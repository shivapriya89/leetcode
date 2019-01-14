class Solution(object):
    def trailingZeroes(self, n):
        prod=1
        for i in range(n,0,-1):
            prod *= i

        count=0
        while prod>0:
            if prod%10==0:
                count += 1
                prod /= 10
            else:
                return count

if __name__=='__main__':
    s=Solution()
    print(s.trailingZeroes(3))