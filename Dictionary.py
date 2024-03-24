# Dictionary: is a collection which is unordered and indexed.
# Indexed by keys 

#Creation with dict contructor and {} braces
my_dict = dict(one='uno',two='dos',three='tres')
print(my_dict)

my_dict2 = {'one':'uno','two':'dos','three':'tres'}
print(my_dict2)

#Tuple to dictionary
my_list = [('one','uno'),('two','dos'),('three','tres')]
my_dict3 = dict(my_list)
print(my_dict3)

#Update or add key value pair in dictionary
my_dict4 = {"ap":"10","ts":"12"}
my_dict4["ap"] = "12" #Updating the element
print(my_dict4)

my_dict4["ka"] = "24" #Adding the element
print(my_dict4)

#Traversing the elements
for key in my_dict4:
    print(key,my_dict4[key])

#Search an element in dictions
def search(dict,key):
    for value in dict:
        if key == value:
            return key, dict[key] 
    return "Not Present"
print(search(my_dict4,"ap"))

#Remove and deleting element
# 1. del method
# 2. .pop()

del (my_dict4["ap"])
my_dict4.pop("ts") # Prints value 
my_dict4.popitem() # Prints key value pair

print(my_dict4)

#### Dictionary methods ###
# dictionary.clear()
# dictionary.copy()  shellow copy of the dictionary
newDict = {}.fromkeys([1,2,3],0)
print(newDict)
