# Import array module, so we need to provide details like module.class arr.array
import array as arr

myarr1 = arr.array('i',[1,2,3,4])

#print(myarr1)
#myarr1.insert(0,6)
#print(myarr1)

#Traversal of array
def traversal(array):
    for element in array:
        print(element)
#traversal(myarr1)

#Accessing element in array
def access(array,index):
    if index >= len(array):
        print("Out of index in array !!")
    else:
        print(array[index])
#access(myarr1,6)
        
#Searching an element in array
def linear_search(array, target):
    for index in range(len(array)):
        if target == array[index]:
            return index
    return -1
#print(linear_search(myarr1,3))

#Deleting an element in array
def delete(array,element):
    array.remove(element)
    print(array)
#delete(myarr1,4)
