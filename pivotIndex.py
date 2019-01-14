def pivotIndex(nums):
    i = 1
    j = len(nums)-2
    sum_i=nums[0]
    sum_j=nums[-1]
    while i < len(nums) and j > -1:
        sum_i += nums[i]
        if sum_i == sum_j and i < j:
            return j
        if sum_i == sum_j and i > j:
            return i
        elif sum_i == sum_j and i == j:
            return i
        elif sum_i != sum_j:
            sum_j += nums[j]
            i += 1
            j -= 1
            continue
    return -1


print(pivotIndex([-1,-1,-1,-1,-1,0]))