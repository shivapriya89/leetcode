class Solution(object):
    def uncommonFromSentences(self, A, B):
        a_list=[word for word in A.split(" ")]
        b_list=[word for word in B.split(" ")]
        res=[]
        for word in a_list:
            if a_list.count(word) == 1 and word not in b_list:
                res.append(word)
        for word in b_list:
            if b_list.count(word) == 1 and word not in a_list:
                res.append(word)
        return res

if __name__=='__main__':
    s=Solution()
    print(s.uncommonFromSentences("this apple is sweet","this sour apple"))
    print(s.uncommonFromSentences("apple apple","banana"))