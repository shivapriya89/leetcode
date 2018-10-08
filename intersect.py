class Solution(object):
    def intersect(self, num1, num2):
        dict1={}
        for num in num1:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1

        dict2={}
        for num in num2:
            if num in dict2:
                dict2[num] += 1
            else:
                dict2[num] = 1

        res=[]
        for num in dict1:
            if num in dict2:
                if dict1[num] == dict2[num]:
                    for i in range (dict1[num]):
                        res.append(num)
                elif dict1[num] < dict2[num]:
                    for i in range (dict1[num]):
                        res.append(num)
                elif dict1[num] > dict2[num]:
                    for i in range (dict2[num]):
                        res.append(num)
            else:
                continue

        return res

if __name__=='__main__':
    s=Solution()
    print(s.intersect([4,9,5],[9,4,9,8,4]))