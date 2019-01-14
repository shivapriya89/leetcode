class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        res=[]
        for word in words:
            if self.patternFind(word,pattern) and self.patternFind(pattern,word):
                res.append(word)
        return res

    def patternFind(self,word,pattern):
        dict={}
        i=0
        while i < len(word):
            if pattern[i] not in dict.keys():
                dict[pattern[i]]=word[i]
            else:
                if dict[pattern[i]]!=word[i]:
                    return False
            i+=1
        return True

if __name__=='__main__':
    s=Solution()
    print(s.findAndReplacePattern(["abc","mee","dkd"],'aba'))