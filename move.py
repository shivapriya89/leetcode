class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        i=0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                count += 1
            else:
                i += 1
            #return count
        for i in range(count):
            nums.append(0)
        return nums

if __name__=='__main__':
    s=Solution()
    print(s.moveZeroes([0,1,0,3,12,0]))
    print(s.moveZeroes([0,0,1]))