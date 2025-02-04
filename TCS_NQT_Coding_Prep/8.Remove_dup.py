def remove_duplicate(nums):
    unique_nums = list(set(nums))
    unique_nums.sort()
    nums[:len(unique_nums)] = unique_nums
    return len(unique_nums)
nums = [1,1,2]
k = remove_duplicate(nums)
print(k , nums[:k])