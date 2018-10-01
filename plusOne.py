class Solution(object):
    def plusOne(self, digits):
        num=0
        j=0
        while j < len(digits):
            for i in range(len(digits)-1,-1,-1):
                num = num + digits[j]*(10**i)
                j += 1
        res = str(num+1)
        l=[]
        for char in res:
            l.append(int(char))
        return l


        """i=len(digits)-1
        num=digits[i]+1
        if num < 10:
            digits.pop(i)
            digits.append(num)
        if num == 10:
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
        return digits"""

if __name__=='__main__':
    s=Solution()
    print(s.plusOne([1,9,2]))
    print(s.plusOne([1,9]))