def collatzSeqGen(max_num):

    #keep track of the number that produced the max sequence (count, num)
    max = (-1,-1)

    for num in range(1,max_num):
        start_num = num #store this so its not lost
        count = 0
        while num is not 1:
            if num % 2 == 0:
                num = num // 2
            else:
                #this 3*n+1 will always be even so we might as well divide by 2 here to save a step
                num = (3 * num + 1) // 2
            count += 1

        #check to see if the last checked number is the new max and update if nessacary
        if count > max[0]:
            max = (count , start_num)
    return max

#Main
print(collatzSeqGen(1000000)[1])