class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict={'P':0,'A':0,'L':0}
        for char in s:
            if char=='P':
                dict['P'] += 1
            if char=='A':
                dict['A'] += 1
            if char=='L':
                dict['L'] += 1

        if dict['A']==0 and dict['L']>2:
            return False
        if dict['L']==0 and dict['A']>1:
            return False
        if dict['A'] > 1 or dict['L'] > 2:
            return False
        elif dict['A'] < 2 and dict['L'] < 3:
            return True

if __name__=='__main__':
    s=Solution()
    print(s.checkRecord('LLLL'))
