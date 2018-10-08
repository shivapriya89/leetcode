class Solution(object):
    def findContentChildren(self, g, s):
        count=0
        for i in range(len(g)):
            for j in range(len(s)):
                if s[j] >= g[i]:
                    count += 1
                    break
                else:
                    continue
        return count

if __name__=='__main__':
    s=Solution()
    print(s.findContentChildren([1,2,3],[1,2]))