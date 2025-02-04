def freq(arr):
    frequency = {}
    for i in arr:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
     

    for key,value in frequency.items():
        print(f"the element is {key} and it's was repeated with the value of {value}")
    return frequency

arr2 = [ 4,4,5,6,7]
freq(arr2)
print(freq(arr2))
 

# arr1 = [ 1,1,2,2,3]
# print(freq(arr1))