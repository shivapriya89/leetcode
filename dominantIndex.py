class Solution(object):
    def dominantIndex(self, nums):
        s_nums = sorted(nums)
        if s_nums[-2]*2 <= s_nums[-1]:
            return nums.index(s_nums[-1])
        else:
            return -1

if __name__=='__main__':
    s=Solution()
    print(s.dominantIndex([0,3,1,6,2]))