def highest_sibling_number(num):
    my_list=[]
    while num > 0:
        my_list.append(num%10)
        num //= 10

    my_list.sort(reverse=True)
    my_str=''.join(str(n) for n in my_list)
    return int(my_str)

print(highest_sibling_number(6739))