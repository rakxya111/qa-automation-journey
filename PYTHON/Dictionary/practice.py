# DICTIONARY

# thisdict = {
#     'brand' : 'Vespa',
#     'colour' : 'Purple',
#     'year' : 1999
# }

# Access the dictionary 

# x = thisdict['brand']
# print(x)

# thisdict['colour'] = 'white'
# print(x)


# Get Keys

# x = thisdict.keys()
# print(x)
# thisdict['year'] = 9900
# print(x)


# Get values

# x = thisdict.values()
# print(x)
# thisdict['brand'] = 'vespa pink'
# print(x)

# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")
# else:
#   print("No, 'model' is one of the keys in the thisdict dictionary")
  

# Update and Change Items

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict.update({'model' : 'Vespa'})
# thisdict["year"] = 2018
# print(thisdict)



# REMOVE from Dictionary

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict.pop('brand')
# print(thisdict)

# ''' removes the last inserted item '''
# thisdict.popitem() 
# print(thisdict)

# thisdict1 = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# del thisdict1['year']
# print(thisdict1)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # Removes the entire dict , shows error if perfomed printing
# del thisdict 

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # empties the dictionary
# thisdict.clear()
# print(thisdict)




# Loop Dictionaries


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# for i in thisdict:
#     print(i)

# for i in thisdict:
#     print(f'{i} : {thisdict[i]}')

# x = thisdict.items()
# print(x)

# for x in thisdict.values():
#     print(x)

# for x in thisdict.keys():
#     print(x)

# for x , y in thisdict.items():
#     print(x, y)


# COPY DICTIONARIES

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# copied_dict = thisdict.copy()
# print(copied_dict)

# new_dict = dict(thisdict)
# print(new_dict)



# Nested Dictionaries

thisdict = {
    "child" : {
        'name' : 'rehaba',
        'age' : 19
    },
    "child1" : {
        'name' : 'naunii',
        'age' : 20
    },
    "child1" : {
        'name' : 'naunii',
        'age' : 20
    }
}
print(thisdict)


# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
    'child1' : child1,
    'child2' : child2,
    'child3' : child3
}
# print(myfamily['child1']['name'])



# Loop Through Nested Dictionaries

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
