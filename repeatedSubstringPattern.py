import math

class Solution(object):
    def repeatedSubstringPattern(self, s):
        check_list = []
        if len(s) == 1:
            return False
        for i in range(1,math.ceil(len(s)/2)+1):
            if len(s)%i == 0:
                check_list.append(i)

        for i in check_list:
            if s[0:i]*math.ceil(len(s)/i) == s:
                return True
        return False

if __name__=='__main__':
    s=Solution()
    print(s.repeatedSubstringPattern('aaa'))