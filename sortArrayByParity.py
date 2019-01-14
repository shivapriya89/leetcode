class Solution(object):
    def sortArrayByParityII(self, A):
        old_len=len(A)
        res=[]
        i=0
        while i <= old_len:
            if i == 0:
                j=0
                while j < len(A):
                    if A[j]%2 == 0:
                        res.append(A[j])
                        A.pop(j)
                        break
                    else:
                        j += 1
                        continue
                i += 1
            if i > 0:
                if i%2 == 0:
                    j=0
                    while j < len(A):
                        if A[j]%2 == 0:
                            res.append(A[j])
                            A.pop(j)
                            break
                        else:
                            j += 1
                            continue
                else:
                    j=0
                    while j < len(A):
                        if A[j]%2 != 0:
                            res.append(A[j])
                            A.pop(j)
                            break
                        else:
                            j += 1
                            continue
                i += 1
                continue
        return res

if __name__=='__main__':
    s=Solution()
    print(s.sortArrayByParityII([4,2,5,7]))