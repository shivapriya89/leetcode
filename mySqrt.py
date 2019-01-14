def mySqrt(x):
    for i in range(x//2+1):
        if i*i == x:
            return x
        elif i*i > x:
            return ((i-1)*(i-1))

print(mySqrt(4))