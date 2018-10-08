class Solution(object):
    def twoSum(self, numbers, target):
        res=[]
        for i in range(len(numbers)):
            #j=i+1
            diff = target-numbers[i]
            num=numbers[i+1::]
            if diff in num:
                res.append(i+1)
                idx=(numbers.index(diff))
                if diff == numbers[i]:
                    res.append(idx+2)
                else:
                    res.append(idx+1)
                break
        return res

if __name__=='__main__':
    s=Solution()
    print(s.twoSum([0,0,3,4],0))
    print(s.twoSum([2,7,11,12],9))