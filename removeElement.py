class Solution(object):
    def removeElement(self, nums, val):
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==val:
                nums.remove(nums[i])
        return len(nums)

if __name__=='__main__':
    s=Solution()
    print(s.removeElement([3,2,2,3,2],2))