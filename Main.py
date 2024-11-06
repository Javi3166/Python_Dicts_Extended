# Dictionary: Key-Value pairs, Unordered, Mutable

print("You can create a dictionary function using {}.")
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

print("\nYou can also create a dictionary using the dict() function.")
mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

print("\nYou can access elements of a dictionary by calling it's keyword.")
print(mydict["name"])

print("\nYou can assign an element to a variable.")
value = mydict["age"]
print(value)

print("\nSince dictionaries are mutable, we can append and edit it.")
mydict["email"] = "max@xyv.xom"
print(mydict)

print("\nWe can edit certain keys by calling it and overriding with a new value.")
mydict["email"] = "coolmax@xyz.com"
print(mydict)

print("\nOne way to delete an element in a dictionary is using the del command.")
del mydict["name"]
print(mydict)

print("\nYou can also use the .pop method to delete an item.")
mydict.pop("age")
print(mydict)

print("\nUsing .popitem will remove the last item in the dictionary.")
mydict.popitem()
print(mydict)

mydict = {"name": "Max", "age": 28, "city": "New York"}

print("\nYou can check if a certain element is in a dictionary by using an if statement.")
if "name" in mydict:
    print(mydict["name"])

print("\nIf you try to access an element that a dictionary does not have, it will throw an error, specifically a key error.")
try:
    print(mydict["lastname"])
except KeyError:
    print("Error.")

print("\nThere's a few ways to loop through a dictionary. One way is looping through the available keys with a for loop.")
for key in mydict:
    print(key)

print("\nYou can use the .keys() method which will return a list with all the keys inside.")
for key in mydict.keys():
    print(key)

print("\nYou can use .values() instead if you want just the values which will also be a list.")
for value in mydict.values():
    print(value)

print("\nIt is possible to print both values at the same time using the .items() method.")
for key, value in mydict.items():
    print(key, value)

print("\nMust be careful when making a copy of a dictionary because they will point to the same location otherwise."
      "\nWhich means when the copy is changed, it will change the original too.")
mydict_copy = mydict
mydict_copy["email"] = "max@xyz.com"
print(mydict)
print(mydict_copy)

mydict.popitem()

print("\nIt is possible to make a copy using the .copy method.")
mydict_copy = mydict.copy()
mydict_copy["email"] = "max@xyz.com"
print(mydict)
print(mydict_copy)

print("\nIt is also possible to make a copy by passing it as an argument for dict().")
mydict_copy = dict(mydict)
mydict_copy["email"] = "max@xyz.com"
print(mydict)
print(mydict_copy)

print("\nIt is possible to update a dictionary with another dictionary using the .update() function.")
mydict_copy.update(mydict2)
print(mydict_copy)

print("\nDictionaries can also use other immutable data types, including tuples.")
mydict = {3: 9, 6: 36, 9: 81}
print(mydict)

print("\nCare must be taken when trying to access a certain index depending on what keys are used, like 0 won't work "
      "\nbecause it will look for the key 0, not index 0.")
print(mydict[3])

print("\nIt's possible to use tuples as keys. It is not possible to use a list since they are mutable, thus possible to change.")
myTuple = (8, 7)
mydict = {myTuple: 15}
print(mydict)