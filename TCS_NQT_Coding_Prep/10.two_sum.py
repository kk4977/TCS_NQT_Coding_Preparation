# # brute force method

# def two_sum(arr,target):
#     result = []
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]+ arr[j] == target:
#                 result.append([i,j])
#     return result if result else []
# arr = [3, 4, -7, 1, 3, 3, 1, -4]
# target = 7
# print(two_sum(arr, target))

# # output prints the result of the indeces as [[0, 1], [1, 4], [1, 5]]

def two_sum(arr, target):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                result.append([arr[i], arr[j]])
    return result if result else []
arr = [3, 4, -7, 1, 3, 3, 1, -4]
target = 7
print(two_sum(arr, target))