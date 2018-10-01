class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        def sum(num):
            count = 0
            while num >= 10:
                r= num%10
                num //= 10
                count += r
            while num < 10:
                count += num
                return count

        count=sum(num)
        while count:
            if count > 10:
                count=sum(count)
            if count == 10:
                return 1
            if count < 10:
                return count

if __name__=='__main__':
    s=Solution()
    print(s.addDigits(708538619))
    print(s.addDigits(199))
    print(s.addDigits(0))
    print(s.addDigits(10))