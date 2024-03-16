def biggest_number(array):
    big_number = array[0]
    for index in range(1,len(array)):
        if array[index] > big_number:
        #if big_number > array[index]:
            big_number = array[index]
    print(big_number) 

nums=(7,2,5,4)
biggest_number(nums)