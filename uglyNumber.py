class Solution(object):
    def isUgly(self, num):
        res=[]
        half=num//2
        for i in range(1,half+1):
            if num%i==0:
                res.append(i)

        primes = []
        for possiblePrime in range(2, num):
            isPrime = True
            for num in range(2, possiblePrime):
                if possiblePrime % num == 0:
                    isPrime = False
                break
            if isPrime:
                primes.append(possiblePrime)
        if 2 in primes:
            primes.remove(2)
        if 3 in primes:
            primes.remove(3)
        if 5 in primes:
            primes.remove(5)

        for x in res:
            if x in primes:
                return False
        return True

if __name__=='__main__':
    s=Solution()
    print(s.isUgly(-2147483648))
    print(s.isUgly(6))