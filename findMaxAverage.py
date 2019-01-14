class Solution(object):
    def findMaxAverage(self, nums, k):
        avg=[]
        sum=0
        if len(nums)==1:
            return nums[0]
        elif len(nums) > 1 and k == 1:
            return max(nums)
        elif len(nums)==k:
            for i in range(len(nums)):
                sum += nums[i]
                return sum/k
        else:
            for i in range(0,len(nums)-k):
                sum = 0
                for j in range(i,i+k):
                    sum += nums[j]
                avg.append(sum/k)
        return max(avg)

if __name__=='__main__':
    s=Solution()
    print(s.findMaxAverage([1,12,-5,-6,50,3],4))
    print(s.findMaxAverage([4,2,1,3,3],2))