class Solution(object):
    def findLengthOfLCIS(self, nums):
        count = 0
        temp = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                temp += 1
                if temp > count:
                    count=temp
                else:
                    continue
            elif nums[i] >= nums[i+1]:
                if temp > count:
                    count=temp
                    temp=1
                    continue
                if temp <= count:
                    temp=1
                    continue
        return count

if __name__=='__main__':
    s=Solution()
    print(s.findLengthOfLCIS([1,2,3,4,5,2,3,1,2,3,4,5,6,7]))
    print(s.findLengthOfLCIS([2,2,2,2]))
    print(s.findLengthOfLCIS([3,0,6,2,4,7,0,0]))
    print(s.findLengthOfLCIS([1,2,3,4]))
    print(s.findLengthOfLCIS([1,3,5,4,7]))