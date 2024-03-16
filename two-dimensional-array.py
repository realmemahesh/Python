# Use-cases: when you are assigned to take readings of temperatures 4 times a day for 4 days.

# Create, Transverse, Append/Add, Search, Delete

import numpy as np

# Creation of 2d array
twodarr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(twodarr)
print("\n")

#Adding element in 2d array o(rc)
newtwodarr =  np.insert(twodarr, 0, [21,22,23,24],axis=0)
print(newtwodarr)
print("\n")

#Appending the 2d array o(rc)
newtwodarr2 =  np.append(twodarr,[[31,32,33,34]],axis=0)
print(newtwodarr2)
#print(len(newtwodarr2))


#Accessing the 2d array
def access_element(arr, rowindex, colindex):
    if rowindex <= len(arr) and colindex <= len(arr[0]):
        print(arr[rowindex,colindex])
    else:
        assert "wrong index provided !!"

access_element(twodarr,10,2)

#Traversing though a 2d array
def traversing(arr):
    for i in range(len(arr)):
      for j in range(len(arr[0])):
        print(arr[i][j])
#traversing(newtwodarr2)

#Searching for a element in array with linear search algo
def search(arr, val):
   for i in range(len(arr)):
      for j in range(len(arr[0])):
         if val == arr[i][j]:
            return "The value present at "+str(i)+" row "+str(j)+" column "
   return "Value may be not present in matrix"
print(search(newtwodarr,10))
print("\n")

#Deletion of row/column in 2d matrix
def deletion(arr,row,axis):
   print(np.delete(arr,row,axis=axis))
deletion(newtwodarr,0,0)
