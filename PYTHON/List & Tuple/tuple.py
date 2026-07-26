# TUPLE - Immutable, heterogeneous (stores multiple data types)

# a = (1, 2, 3, 4) 
# b = ()
# print(type(a))
# print(type(b))
# print(a)

# # Demonstrating homogeneous tuples
# fruits = ("apple", "banana", "cherry")
# numbers = (1, 5, 7, 9, 3)
# booleans = (True, False, False)

# # Demonstrating a HETEROGENEOUS tuple (multiple data types)
# mixed_tuple = ("Python", 2026, True, 9.99)

# print(fruits)
# print(mixed_tuple)

# # len , min max , count , index() , sorted()



x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "Hazmola"
x = tuple(y)

print(x)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)