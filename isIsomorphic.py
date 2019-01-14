class Solution(object):
    def isIsomorphic(self, s, t):
        dict={}
        for i in range(len(s)):
            if s[i] not in dict and t[i] not in dict.values():
                dict[s[i]]=t[i]
            elif s[i] not in dict and t[i] in dict.values():
                return False
            else:
                if t[i] != dict[s[i]]:
                    return False
                elif t[i] == dict[s[i]]:
                    continue
        return True

if __name__=='__main__':
    s=Solution()
    #print(s.isIsomorphic('add','egg'))
    #print(s.isIsomorphic('foo','bar'))
    print(s.isIsomorphic('paper','title'))
    print(s.isIsomorphic('ab','aa'))