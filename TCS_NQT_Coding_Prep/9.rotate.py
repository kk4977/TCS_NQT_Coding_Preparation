def rotate(nums, k):
    k = k % len(nums)  # Handle cases where k > len(nums)
    
    # Reverse the entire array
    nums.reverse()
    
    # Reverse the first k elements
    nums[:k] = reversed(nums[:k])
    
    # Reverse the remaining elements
    nums[k:] = reversed(nums[k:])
    
# Example usage
nums = [1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13]
k = 3
rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]


# def rotate(arr,k):
#     arr.reverse()

#     arr[:k] = reversed(arr[:k])
#     arr[k:] = reversed(arr[k:])
# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# rotate(nums, k)
# print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
