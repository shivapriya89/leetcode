class Solution(object):
    def judgeCircle(self, moves):
        i=0
        j=0
        for char in moves:
            if char=='R':
                i += 1
                #continue
            if char=='L':
                i -= 1
                #continue
            if char=='U':
                j += 1
                #continue
            if char=='D':
                j -= 1
                #continue
        if i == 0 and j == 0:
            return True
        else:
            return False

if __name__=='__main__':
    s=Solution()
    print(s.judgeCircle('LDUR'))
    print(s.judgeCircle('LDU'))