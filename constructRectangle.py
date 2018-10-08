class Solution(object):
    def constructRectangle(self, area):
        res=[]
        j=0
        for i in range(1,area//2+1):
            if area%i == 0:
                res.append([])
                res[j].append(i)
                res[j].append(int(area/i))
            else:
                continue
            j += 1
        res.append([area,1])

        diff=[]
        for i in range(len(res)):
            diff.append(abs(res[i][0]-res[i][1]))
        idx=diff.index(min(diff))

        if res[idx][0] < res[idx][1]:
            res[idx][0],res[idx][1]=res[idx][1],res[idx][0]
        return res[idx]

if __name__=='__main__':
    s=Solution()
    print(s.constructRectangle(30))