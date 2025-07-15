#Python Dictionaries - like js object
friends = {
    'name': 'Utsab',
    'age': 22 
}

# name vanney key xa ki nai check gareko
if 'name' in friends:
    print("xa")

del friends['age']

# adding new key in Dictionaries
friends['isNepali']=True
friends['address']="Nepal"

# print(friends['age'])
print(friends['isNepali'])

print(friends.keys(), friends.values())

#Python Tuple = immutable, can't change anything
my_typle = (1,2,3, "bishal", 3.14)

# It ignore duplicacy
my_set = {1,2,3,21,1}
print(my_set)