class Solution(object):
    def findComplement(self, num):
        num=format(num,'b')
        s=''
        for char in num:
            if char=='1':
                s+=('0')
            if char=='0':
                s+=('1')
        return int(s,2)

if __name__=='__main__':
    a=Solution()
    print(a.findComplement(5))