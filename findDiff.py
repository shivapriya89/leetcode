class Solution(object):
    def findTheDifference(self, s, t):
        dict={}
        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
        for char in t:
            if char in dict:
                dict[char] -= 1
            else:
                dict[char] = 1

        for char in dict:
            if dict[char] != 0:
                return char

if __name__=='__main__':
    s=Solution()
    print(s.findTheDifference('abcd','bcdae'))
    print(s.findTheDifference('a','aa'))