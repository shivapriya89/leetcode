class Solution(object):
    def findLHS(self, nums):
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        #print(dict)
        res=0
        for num in dict:
            if num-1 in dict:
                temp=dict[num]+dict[num-1]
                if temp > res:
                    res=temp
        return res

if __name__=='__main__':
    s=Solution()
    print(s.findLHS([1,3,2,2,5,2,3,7]))
    print(s.findLHS([1,0,0,0,1,2,2]))