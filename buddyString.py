def buddyStrings(A, B):
    if len(A) != len(B):
        return False
    unmatched = 0
    a=[]
    b=[]
    for i in range(len(A)):
        if A[i] != B[i]:
            unmatched += 1
            a.append(A[i])
            b.append(B[i])
    if unmatched == 2:
        if a[0] == b[-1] and b[0] == a[-1]:
            return True
        else:
            return False
    if unmatched != 2:
        return False

print(buddyStrings('acb','abd'))