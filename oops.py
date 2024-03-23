# Class, Methods, Attributes and Objects

# what it is ?(className), What it has ?(Attributes), What it does ? (Methods/Functions)

# Class is code template for creating the object

# Nameing conventions - PascalCase, camelCase, snake_case

class Youtube:
    def __init__(self,username,subscritions=0,subscribers=0):
        self.username = username
        self.subscritions = subscritions
        self.subscribers = subscribers
    
    def add_subscriptions(self,user_obj):
        self.subscritions += 1 
        user_obj.subscribers += 1

user1 = Youtube("Mahesh")
print(f"User1 subscritions {user1.subscritions} and subscibers {user1.subscribers}")

user2 = Youtube("Krishna")
user2.add_subscriptions(user1)
print(f"User2 subscritions {user2.subscritions} and subscibers {user2.subscribers}")
print(f"User1 subscritions {user1.subscritions} and subscibers {user1.subscribers}")
