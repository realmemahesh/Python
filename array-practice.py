#From array module import all classes
from array import *

#1. Create an array and transverse
myarr1 = array('i',[1,2,3,4])
for i in myarr1:
    print(i)

#2. Access individual element through index
print("\nstep2")
print(myarr1[0])

#3. Append any value of the array using append() method at last
myarr1.append(6)
print(myarr1)

#4.Insert a value in the array using Insert() method at any where
myarr1.insert(4,10)
print(myarr1)

#5. Extend python array with extend() method with another array at end of array
myarr1.extend([11,12,13])
print(myarr1)

#6. Add the list into the array by using fromlist() method.
list1=[1,3,4,5]
myarr1.fromlist(list1)
print(myarr1)

#7. Remove an element in array using remove() method but it remove first occurance.
myarr1.remove(12)
print(myarr1)

#8. Remove last element of the array using pop()
myarr1.pop()
print(myarr1)

#9. Reverse an array using reverse()
myarr1.reverse()
print(myarr1)

#10. convert int array to string array
# strarr = myarr1.tostring()
# print(strarr)
# intarr = array('i')           #Empty array
# intarr.fromstring(strarr)
# print(intarr)

#11. convert array to list
print(myarr1.tolist())

#12. slicing the array
print(myarr1[1:]) #starting from 1st index
print(myarr1[:6]) #till 6th index
print(myarr1[:])  #All elements