def countDuplicates(numbers):
    dict={}
    count = 0
    for num in numbers:
        if num not in dict:
            dict[num]=1
        else:
            dict[num]+=1
            if dict[num] == 2:
                count += 1
            else:
                continue
    return count

print(countDuplicates([1,2,2,2,3,4,5,5,4,2]))