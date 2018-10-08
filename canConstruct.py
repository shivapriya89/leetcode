class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dict1={}
        dict2={}
        for char in magazine:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1

        for char in ransomNote:
            if char in dict2:
                dict2[char] += 1
            else:
                dict2[char] = 1

        for char in dict2:
            if (char not in dict1) is True:
                return False
            if dict1[char] < dict2[char]:
                return False
        return True

if __name__=='__main__':
    s=Solution()
    print(s.canConstruct('ab','aaa'))
    print(s.canConstruct('aa','aab'))