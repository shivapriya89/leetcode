def countPrimes(n):
    prime_list = [1] * n
    for num in range(n):
        if num < 2:
            prime_list[num] = 0
        elif prime_list[num]:
            for i in range(2, (n-1)//num+1):
                prime_list[num*i] = 0
    return sum(prime_list)

print(countPrimes(10))