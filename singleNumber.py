class Solution(object):
    def singleNumber(self, nums):
        res=[]
        for num in nums:
            if num not in res:
                res.append(num)
                continue
            elif num in res:
                res.remove(num)
        return res[0]

if __name__=='__main__':
    s=Solution()
    print(s.singleNumber([2,2,1]))
    print(s.singleNumber([1,2,3,4,3,2,2,2,1,1,1,3]))