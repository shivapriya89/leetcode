class Solution(object):
    def hammingDistance(self, x, y):
        count = 0
        if y < x:
            x, y = y, x

        xbit = ('0' * (len(bin(y)) - len(bin(x))) + bin(x)[2:])
        ybit = bin(y)[2:]

        for i in range(len(xbit)):
            if xbit[i] != ybit[i]:
                count += 1

        return count

if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1, 4))
    print(s.hammingDistance(64, 2))
