
def search1(arr,target):
 
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1     
   
   
target  = 6
arr2 = [4,5,6,7]
print(search1(arr2,target))

arr1 = [1,2,3]
print(search1(arr1,target))