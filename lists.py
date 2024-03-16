#list: we can create lists in lists and which holds ordered collections of items/elements of different or same type.

shopping_list = ['milk','chocolates','icecream']
print('milk' in shopping_list)

# Traversing thought a list
for i in shopping_list:
    print(i)

# Traversing with range function
for i in range(len(shopping_list)):
    shopping_list[i] = shopping_list[i]+" Indian"
    print(shopping_list[i])

# Update/Insert( insert or append or extend ) a element in list
    
# 1.update type
shopping_list[0]='coffee'
print(shopping_list)

# 2. Insert by insert or append or extend methods
shopping_list.insert(1,"Cool Drink")
print(shopping_list)

shopping_list.append("TEA")  
print(shopping_list)

new_items=["bike","car"]
shopping_list.extend(new_items)
print(shopping_list)

# Slicing and Deleting ( Pop or Delete or remove )elements in list
int_list=[1,2,3,4,5]
int_list[2:]=[9,8,7,6]
print(int_list)

print(int_list.pop()) # Pop will displays the deleted elements

del int_list[:1]   # Deleting the element based on index
print(int_list)

int_list.remove(7)  # removing the particular element
print(int_list)

# Searching for a element in list
def search_in(list,ele):
    if ele in list:
        print(f"Element {ele} is present in list")
    else:
        print(f"Element {ele} is not present in list")

def linear_search(list,ele):
    for index, value in enumerate(list):
        if ele == value:
            return index
    return -1

print(linear_search(int_list,9))

# List operators / functions

a = [1,2,3]
b = [4,5,6]

print(a+b)      # + operator concatenates the list as if extends
print(a*2)      # * operator multiplies the list as iteration
print(len(a))   # len() function to print length of list
print(max(a))   # max() function to print max num of list
print(min(a))   # min() function to print min num
print(sum(a))   # sum() sums the numbers in list

# total = 0
# count = 0
# while (True):
#     inp = input("Enter the num:")
#     if inp == "done": break  #Breaking condition
#     value = float(inp)
#     total = total + value
#     count = count + 1
#     average =  total/count
# print(f"Average is {average}")
1
my_list = []
while(True):
    inp = input('Enter the num: ')
    if inp == "done": break
    value = float(inp)
    my_list.append(value)
    average = sum(my_list)/len(my_list)
print(f"Average is {average}")