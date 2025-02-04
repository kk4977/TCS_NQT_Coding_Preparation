def find_unq(arr):
    result = 0
    for i in arr:
        result = result^i
    return result
arr1 = [1,2,2,3,3,5,5,6]
print (find_unq(arr1))
