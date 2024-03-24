# linked list :
# A linked list is a type of linear data structure similar to arrays. 
# It is a collection of nodes that are linked with each other.
# is not contiguous whereas list is contiguous

#Types:
# 1. Singuly linkedlists
# 2. Doubly linked lists  --> music player
# 3. Circular singly linked lists  --> 4 player chess
# 4. Circular doubly linked list  --> shifing between applications

#Terminology:
# Node, {data,point to adjecent element}
# Head and Tail
# null

#Creation of linkedlist
# Create a class to create node #Host data and pointer to next node

# Created Node (ele,next_val)
# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# to create linked list (head , tail)
# class LinkedList:
#     def __init__(self,value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

# new_linked_list = LinkedList(10)
# print(new_linked_list.head.value)
# print(new_linked_list.tail.next)

#Data insertion in linked list
# 1. Insertion at the beginning
# 2. In the middle of linked list
# 3. At the End of linked list

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # Print linked list
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
              result += '-->' 
            temp_node = temp_node.next
        return result
    
    # Add node at first 
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    # Add element at any index
    def insert(self,value,index):
        new_node = Node(value)
        temp_node = self.head
        if index < 0 or index > self.length:
          return False
        elif self.head == None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length +=1
        return True
    
    # Traverse the linked list
    def traverse(self):
        temp_node = self.head
        while temp_node is not None:
            print (f"Node value: {temp_node.value}")
            temp_node = temp_node.next

    # Search an element in linkedlist
    def search(self,target):
        temp_node = self.head
        index = 0
        while temp_node:
            if temp_node.value == target:
                return index
            temp_node = temp_node.next
            index += 1
        return -1

    # get and print value
    def get(self,index):
        temp_node = self.head
        if index > self.length:
            return -1
        for i in range(index):
            if i == index-1:
                return temp_node
            temp_node = temp_node.next

    # set the value at index
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # pop the first element
    def pop_first(self):
        if self.length == 0 :
            return None
        pop_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = pop_node.next
            pop_node.next = None
        self.length -= 1
        return pop_node
    
    # pop the last node
    def pop(self):
        if self.length == 0:
            return None
        pop_node = self.tail
        temp_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
        self.length -= 1
        return pop_node   
    
    # Remove node in between linked list
    def remove (self, index):
        if index >=self.length or index < -1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1 or index == -1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = self.get(index)
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1

    # Delete all
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0   # Garbage collector deletes all the elements since no element is pointing to head and tail


new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.prepend(30)
new_linked_list.insert(50,2)
print(new_linked_list)
new_linked_list.traverse()
print(new_linked_list.search(20))
new_linked_list.get(2)
new_linked_list.set_value(2,100)
print(new_linked_list)
print(new_linked_list.pop_first())
print(new_linked_list)
new_linked_list.pop()
print(new_linked_list)
new_linked_list.remove(-1)
print(new_linked_list)