class Solution(object):
    def findWords(self, words):
        r1=['q','w','e','r','t','y','u','i','o','p']
        r2=['a','s','d','f','g','h','j','k','l']
        r3=['z','x','c','v','b','n','m']
        res=[]
        for word in words:
            count_r1=0
            count_r2=0
            count_r3=0
            l_word=word.lower()
            for i in range(len(l_word)):
                if l_word[i] in r1:
                    count_r1 += 1
                if l_word[i] in r2:
                    count_r2 += 1
                if l_word[i] in r3:
                    count_r3+=1
            if len(l_word)==count_r1 or len(l_word)==count_r2 or len(l_word)==count_r3:
                res.append(word)
        return res

if __name__=='__main__':
    s=Solution()
    print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
    #print(s.findWords(['red','dad']))