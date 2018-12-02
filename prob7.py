import math

CASE1 = [1,13,17,29,37,41,49,53]
CASE2 = [7,19,31,43]
CASE3 = [11,23,47,59]


def atkin(max_num):
    
    #to upt o and includeing the max num
    max_num += 1

    #create the initial results list
    res = [2,3,5]

    #initizalize the sieve
    sieve = [-1] * (max_num + 1)

    #begin the sieve
    for x in range(math.ceil(math.sqrt(max_num))):
        for y in range(math.ceil(math.sqrt(max_num))):

            #calculate the n's
            n1 = 4*int(math.pow(x,2)) + int(math.pow(y,2))
            n2 = 3*int(math.pow(x,2)) + int(math.pow(y,2))
            n3 = 3*int(math.pow(x,2)) - int(math.pow(y,2))
            
            #evauluate their results
            if n1 <= max_num and (n1 % 12 == 1 or n1 % 12 == 5):
                sieve[n1] *= -1;
            if n2 <= max_num and n2 % 12 == 7:
                sieve[n2] *= -1;
            if n3 <= max_num and x > y and n3 % 12 == 11:
                sieve[n3] *= -1;

    #TODO: what does this do?
    for x in range(5,math.ceil(math.sqrt(max_num))):
        if sieve[x] == 1:
            z = int(math.pow(x,2))
            for y in range(x,max_num,z):
                if sieve[y] == 1:
                    sieve[y] *= -1


    return (res + [num for num in range(6,len(sieve)) if sieve[num] == 1])

#call it
print(atkin(10001)[-1:])

