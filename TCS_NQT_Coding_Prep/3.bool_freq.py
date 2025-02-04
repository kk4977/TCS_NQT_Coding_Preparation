def freq(arr):
###########################################################approch-1############################################
    # frequency = {}
    # for i in arr:
    #         if i in frequency:
    #             frequency[i] += 1
    #         else:
    #             frequency[i] = 1
     

    # for key,value in frequency.items():
    #     if value == 1:
    #         print(f"the element is {key} and it's was repeated with the value of {value}")
    #         return key
    # return False
  ####################################approch 2   #########################################
    temp = []
    for i in range(len(arr) - 2):
        if arr[i] != arr[i + 1] & arr[i + 1] != arr[i+2]:
            
            temp.append(arr[i+1])
    return temp
arr2 = [4,4,5,6,7]
freq(arr2)
print(freq(arr2))
 

arr1 = [1,2,3]
print(freq(arr1))