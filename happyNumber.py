class Solution(object):
    def isHappy(self, n):
        if n == 0:
            return False
        if n < 4 and n != 1:
            return False
        if n == 1:
            return True

        def findSum(num):
            sum=0
            while num > 9:
                r=num%10
                sum += r**2
                num //= 10
            if num < 10:
                sum += num**2
            return sum

        sum=findSum(n)
        if sum > 10:
            sum=findSum(sum)
        else:
            if sum == 1 or sum == 7:
                return True
            else:
                return False

if __name__=='__main__':
    s=Solution()
    print(s.isHappy(1111111))
    print(s.isHappy(4))