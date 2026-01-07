# 3 ways we can call dictionaries

my_dict = {"mithun": "shetty", 'pavan': 'test'}
print(my_dict)

# using dict constructor
student = dict (mithun="shetty", pavan="test")
print(student)


#using tuple
person2 = dict ([('name', 'mithun'), ('age', 25)])
print(person2)


print(type(person2))

#to get the valueof that key
print(person2.get("name"))

# to get all values in dictionary
print(person2.values())

#to get all key and values in dictionary
print(person2.items())

#to get all the keys in dictionary
print(person2.keys())






# to delete the item

del person2['name']

print(person2)

# to add new item to dictionary

person2["mithun"] = "shetty"

print(person2)

#pop is also used to delete the item but we can see the deleted item

test1 = person2.pop("mithun")
print(test1)
print(person2)