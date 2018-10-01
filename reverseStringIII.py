class Solution(object):
    def reverseString(self, s):
        separate_s = s.split(' ')
        #print(separate_s)
        for i in range(len(separate_s)):
            separate_s[i]=separate_s[i][::-1]
        return ' '.join(separate_s)

if __name__=='__main__':
    s=Solution()
    print(s.reverseString("this is my string"))