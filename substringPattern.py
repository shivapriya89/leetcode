def repeatedSubstringPattern(str):
    if not str:
        return False

    ss = (str + str)
    return ss.find(str) != -1

print(repeatedSubstringPattern('aab'))