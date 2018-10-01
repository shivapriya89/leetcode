class Solution(object):
    def shortestToChar(self, S, C):
        small=[]
        big=[]
        count=0
        t_count=0
        for char in S:
            if C == char:
                small.append(t_count)
            t_count += 1
            big.append(count)
            count += 1

        temp=[]
        res=[]
        for i in big:
            for j in small:
                temp.append(abs(i-j))
            res.append(min(temp))
            temp=[]
        return res

if __name__=='__main__':
    s=Solution()
    print(s.shortestToChar('leetcode','e'))