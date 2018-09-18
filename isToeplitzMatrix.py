class Solution(object):
    def isToeplitzMatrix(self, matrix):
        row=len(matrix)
        col=len(matrix[0])
        if row == 1 and col == 1:
            return True

        if row == 1 and col != 1:
            return True

        if col == 1 and row != 1:
            return True

        for i in range(row):
            for j in range(col):
                if i+1 >= row or j+1 >= col:
                    continue
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                else:
                    continue
        return True

if __name__=='__main__':
    s=Solution()
    print(s.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
    print(s.isToeplitzMatrix([[1,2],[2,2]]))
    print(s.isToeplitzMatrix([[11,74,0,93],[40,11,74,7]]))