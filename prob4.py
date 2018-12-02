min_num = 100
max_num = 999
max_pal = -1

#evaluates if a string is a palindrome
def isPalindrome(string):
    return string == string[::-1]

#get all the products and evaluates them
for num1 in range(min_num,max_num+1):
    for num2 in range(min_num,max_num+1):
        p = num1 * num2
        if isPalindrome(str(p)) and p > max_pal:
            max_pal= p

print(max_pal)
