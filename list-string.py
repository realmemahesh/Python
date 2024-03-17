# String to list

string = "Hello to the Programming world"
str_list = string.split()
print (str_list)

string2 = "Hello-From-Program"
delimineter = "-"
str_list2 =  string2.split(delimineter)
print(str_list2)

#List to string

list_from_str = delimineter.join(str_list2)
print(list_from_str)
list_from_str_2 = " ".join(str_list)
print(list_from_str_2)

#Pitfalls in python lists
my_list = [1,2,5,4,3]
original_list = my_list[:] #taking copy of original list
print(my_list.sort())  # returns none. Hence need to read the python documentation
print(my_list)         # which returns the sorted values

###Lists vs Arrays###
# Both data structures are mutable i.e changable
# Both are indexed and iterated though
# They can be sliced
# Arrays for arthematic operations

import numpy as np

myarray = np.array([1,2,3,4])
mylist  = [1,2,3,4]

print(myarray/2)  #Arthematic operations can be done
#print(mylist/2)   # Throughs error

myarray = np.array([1,2,3,4,"a"]) # same data types as string
mylist  = [1,2,3,4,"a"]           # Different data types

# List Comprehension
mylist = [1,2,3,4]
new_list = [i*2 for i in mylist]
print(new_list)

string = "python"
new_str_list = [letter.upper() for letter in string]
print(new_str_list)

# List comprehension with conditions
prev_list = [-1,10,2,-20,40]
new_list = [negnum for negnum in prev_list if negnum < 0]
print(new_list)

sentence = "My World"
def is_consonant(val):
    vowels='aeiou'
    return val.isalpha() and val.lower() not in vowels

consonents = [i for i in sentence if is_consonant(i) ]
print(consonents)

list_1 = [1,-2,3,-4]
def neg_check(val):
    return val if val < 0 else "Positive number"
list_2 = [neg_check(num) for num in list_1 ]
print(list_2)

# [val if condition else condition for loop]
# [function for loop]

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
    
    for row in m:
        for element in row:
            if v < element: return v == element
fun(data[0])

a=[1,2,3,4,5]
print(a[3:0:-1])