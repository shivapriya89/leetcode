class Solution(object):
    def arrangeCoins(self, n):
        count =0
        for i in range(1,n):
            count  += i
            if count < n:
                continue
            elif count == n:
                return i
            elif count > n:
                return i-1

if __name__=='__main__':
    s=Solution()
    print(s.arrangeCoins(876))