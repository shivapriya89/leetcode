class Solution(object):
    def reverseOnlyLetters(self, S):
        my_list=list(S)
        my_str='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        i=0
        j=len(S)-1
        while i <= j and j >= i:
            if my_list[i] in my_str and my_list[j] in my_str:
                my_list[i],my_list[j]=my_list[j],my_list[i]
                i += 1
                j -= 1
            elif my_list[i] in my_str and my_list[j] not in my_str:
                j -= 1
                continue
            elif my_list[i] not in my_str and my_list[j] in my_str:
                i += 1
                continue
            elif my_list[i] not in my_str and my_list[j] not in my_str:
                i += 1
                j -= 1
        return "".join(my_list)

if __name__=='__main__':
    s=Solution()
    print(s.reverseOnlyLetters('Test1ng-Leet=code-Q!'))