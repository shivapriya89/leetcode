class Solution(object):
    def pointsInLine(self,x1,y1,x2,y2,x3,y3):
        if ((y2-y1)/(x2-x1)) == ((y3-y1)/(x3-x1)):
            return True
        else:
            return False

if __name__=='__main__':
    s=Solution()
    print(s.pointsInLine(0,0,1,1,2,2))
    print(s.pointsInLine(0,0,1,1,2,3))