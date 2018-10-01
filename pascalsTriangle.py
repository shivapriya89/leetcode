import math

class Solution(object):
    def getRow(self, rowIndex):
        def binCoef(a,b):
            return int(math.factorial(a) / (math.factorial(b) * math.factorial(a-b)))

        res = [0] * (rowIndex+1)
        for i in range(rowIndex+1):
            if i <= (rowIndex+1)//2:
                res[i] = binCoef(rowIndex,i)
            else:
                res[i] = (res[rowIndex -i])
        return res

if __name__=='__main__':
    s=Solution()
    print(s.getRow(6))
    print(s.getRow(8))