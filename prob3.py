#get the largest prime factor of a value
def largestPrimeFactor(max_val): 

    curr = 2
    while (curr * curr) <= max_val:
        while max_val > 1:
            if max_val % curr != 0:
                curr += 1
            else:
                max_val = max_val // curr

    return curr
            
        

print(largestPrimeFactor(600851475143))

