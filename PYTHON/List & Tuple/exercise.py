'''
3. Lists
 - append(), remove(), pop(), indexing, slicing, loops
 Exercises:
 1. Create a list of 5 browsers.
 2. Add Edge.
 3. Remove Firefox.
 4. Print all browsers using a loop.
 5. Find length.
'''

# browsers = ["chrome", "brave" , "microsoft" , "firefox", "opera"]

# browsers.append("edge")
# browsers.remove("firefox")

# for i in browsers:
#     print(i)

# print(len(browsers))



# INSERT ITEMS IN THE LIST


# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thistuple = ("test1", "test2","kiwi")

# thislist[0] = "mango"
# thislist[1:3] = ["orange","cherry"]
# thislist.insert(1,"guava")
# thislist.append("hello")
# thislist.extend(tropical)
# thislist.extend(thistuple)

# print(thislist)



# Remove the items from the list

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]

# thislist.remove("apple")
# thislist.pop(1)
# del thislist[3]

# print(thislist)

# tropical.clear()
# print(tropical)


# List Comprehension

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]

# new = [i for i in thislist if i != "apple"]
# newmew = [j if j != "mango" else "kiwi" for j in tropical]
# print(new)
# print(newmew)

# newlist = [x for x in thislist if "a" in x]
# newlist1 = [x for x in tropical if x != "mango"]
# newlist2 = [x if x == 'orange' else 'kiwi' for x in list]
# print(newlist)
# print(newlist1)




# Sorting

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist_num = [100, 50, 65, 82, 23]
# thislist_num.sort()
# print(thislist_num)

# thislist.sort(reverse = True)
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = lambda x : x % 10 == 0)
# print(thislist)

# thislist1 = ["banana", "Orange", "Kiwi", "cherry"]
# thislist1.sort(key = str.lower)
# print(thislist1)

# thislist2 = ["banana", "Orange", "Kiwi", "cherry"]
# thislist2.reverse()
# print(thislist2)




# COPY LIST

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# thislist1 = ["apple", "banana", "cherry"]
# mylist1 = list(thislist1)
# print(mylist1)

# thislist2 = ["apple", "banana", "cherry"]
# mylist2 = thislist2[:]
# print(mylist2)


# Join Two Lists

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# for x in list2:
#     list1.append(x)

# print(list1)


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# tup = tuple(list1)
# print(tup)






