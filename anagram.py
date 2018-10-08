class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        if s == '' and t == '':
            return True

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
                return False
        return True

if __name__=='__main__':
    s=Solution()
    #print(s.isAnagram('anagram','nagaram'))
    #print(s.isAnagram('',''))
    print(s.isAnagram('rat','car'))