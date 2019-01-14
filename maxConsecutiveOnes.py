class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        temp = 0
        i=0
        while i < len(nums):
            if nums[i] == 0:
                count = 0
                i += 1
                continue
            else:
                count += 1
                i += 1
                if count > temp:
                    temp = count
        return temp

if __name__=='__main__':
    s=Solution()
    print(s.findMaxConsecutiveOnes([1,1,0,1,1,1,0,1,1,1,1]))