class Solution(object):
    def removeDuplicates(self,nums):
        if len(nums) < 2: return len(nums)
        i = 1
        j = 1
        while(i<len(nums)):
            if nums[i] == nums[i-1]:
                i += 1
            else:
                #nums[j] = nums[i]
                j += 1
                i += 1
        return j

if __name__=='__main__':
    s=Solution()
    print(s.removeDuplicates([0,0,0,2]))