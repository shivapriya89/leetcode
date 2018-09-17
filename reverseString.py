class Solution(object):
    def reverseString(self, s):
        res=''
        for i in range (len(s)-1,-1,-1):
            res+=(s[i])
        return res

if __name__=='__main__':
    s=Solution()
    print(s.reverseString(" hello nsp's "))