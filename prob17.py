numstostring_dict = {
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine"
}

for num in range(1,1001):

    num_str = str(num)
    english_num= ""

    #check thousands
    if num > 999:
        english_num = numstostring_dict[num_str[len(num_str)]] + " thousand "
        
    #check hundreds
    if num > 99:
        

    #check tens
    if num > 9:

    #check ones
    else: