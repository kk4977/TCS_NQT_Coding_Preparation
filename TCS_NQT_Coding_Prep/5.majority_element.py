from collections import Counter
def majorityElement(arr):
    n = len(arr)
    counter = Counter(arr)
    for num,count in counter.items():
        if count > n//2:
            return num
    return -1

arr = [2, 2, 1, 1, 1, 2,1]
ans = majorityElement(arr)
print("The majority element is:", ans)



















# def majorityElement(arr):
#     arr.sort()
#     return arr[len(arr) // 2] 
# arr1 = [3, 2, 3]
# print(majorityElement(arr1))  # Output: 3

# nums2 = [2, 2, 1, 1, 1, 2, 2]
# print(majorityElement(nums2))  # Output: 2