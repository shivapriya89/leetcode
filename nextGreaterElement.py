class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        res=[]
        for x in findNums:
            if x == max(nums):
                res.append(-1)
                continue
            if x in nums and nums.index(x)<=(len(nums)-2):
                ind=nums.index(x)
                for i in range(1,(len(nums)-ind)):
                    if x > nums[ind+i] and (ind+i) > len(nums):
                        continue
                    elif x > nums[ind+i] and (ind+i) == len(nums)-1:
                        res.append(-1)
                        break
                    elif x < nums[ind+i]:
                        res.append((nums[ind+i]))
                        break
                continue
            if nums.index(x)==(len(nums)-1):
                res.append(-1)
                continue
        return res

if __name__=='__main__':
    s=Solution()
    print(s.nextGreaterElement([4,1,2],[1,3,4,2]))
    print(s.nextGreaterElement([2,4],[1,2,3,4]))
    print(s.nextGreaterElement([1,3,5,2,4],[5,4,3,2,1]))
    print(s.nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7]))