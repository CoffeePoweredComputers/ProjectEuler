def getDivisorCount(num):
    divisor_count = 0
    for i in range(1,num):
        if num % i == 0:
            divisor_count += 1
    if divisor_count > 50:
         print(divisor_count)
    return divisor_count



def getTriangle(num_divisors):

    triangle_num = 1

    while getDivisorCount(triangle_num) <= 500:
        triangle_num += 1

    return triangle_num


#MAIN
getDivisorCount(5000000000)