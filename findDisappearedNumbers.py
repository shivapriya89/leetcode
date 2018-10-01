class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums=sorted(nums)
        res=[]
        for i in range(1,nums[-1]):
            if i not in nums:
                res.append(i)
        return res


if __name__=='__main__':
    s=Solution()
    print(s.findDisappearedNumbers([4,3,5,2,6,1,8,10]))