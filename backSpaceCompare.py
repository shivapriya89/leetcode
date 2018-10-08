class Solution(object):
    def backspaceCompare(self, S, T):
        s = []
        t = []

        for i in S:
            if i == '#' and s:
                s.pop()
            elif i != '#':
                s.append(i)

        for i in T:
            if i == '#' and t:
                t.pop()
            elif i != '#':
                t.append(i)

        if s == t:
            return True

        return False

if __name__=='__main__':
    s=Solution()
    print(s.backspaceCompare('a##c','c'))