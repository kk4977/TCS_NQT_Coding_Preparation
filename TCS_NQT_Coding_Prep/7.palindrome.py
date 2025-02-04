def palindrome(num):
    num_str= str(num)
    if num_str == num_str[::-1]:
        return True
    return False
    

num = 129
ans = palindrome(num)
print("The palindrome number is", num , "is", ans)