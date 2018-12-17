from math import *


#uses euclids method for generating pythagorean tripplets
def findTripplet():

    for m in range(0,100):
        for n in range(0,100):
            a=m**2 - n**2
            b=2*m*n
            c=m**2 + n**2
            if (a + b + c) == 1000 and a > 0 and b > 0 and c > 0:
                print("Tripplets:",a,b,c)
                return a, b, c


    return -1,-1,-1



#Main
trip_tup = findTripplet()
product = trip_tup[0] * trip_tup[1] * trip_tup[2]

print(product)

