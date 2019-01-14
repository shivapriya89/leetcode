class Solution(object):
    def firstUniqChar(self, s):
        if len(s) == 1:
            return 0
        dict={}
        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1

        for char in dict:
            if dict[char] == 1:
                return s.index(char)
        return -1

if __name__=='__main__':
    s=Solution()
    print(s.firstUniqChar('ltdehleetcodev'))