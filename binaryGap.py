class Solution(object):
    def binaryGap(self, N):
        n_bin=str(bin(N))
        for i in range(len(n_bin)):
            if n_bin[i] == '1':
                j=i+1
                while j < len(n_bin):
                    if n_bin[j] == '1':
                        return j-i
                    else:
                        j+=1
        return 0


if __name__=='__main__':
    s=Solution()
    print(s.binaryGap(13))