class Solution(object):
    def majorityElement(self, nums):
        dict={}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 0

        for num in dict:
            if dict[num] > (len(nums)//2) or dict[num] == (len(nums)//2):
                return num

if __name__ == '__main__':
    s=Solution()
    print(s.majorityElement([3,3,4]))