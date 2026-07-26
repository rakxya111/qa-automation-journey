# Functions 

# def grettings(name , deisgnation):
#     print(f'My name is {name} and i am a {deisgnation} Automation Engineer.')
   

# grettings('Rakshya Bhuju', deisgnation='QA')

# def practice ():
#     return 'hello world !!!'

# grettings = practice()
# print(practice())

# def children(*child):
#     print("My children names are : ", child)

# children('fedrick','ryan','stefan')

# def children(*args):
#     print(type(args))
#     print("First Argument :", args[0])
#     print("My children names are : ", args)

# children('fedrick','ryan','stefan')


# def my_function(gretting, *names):
#     for name in names:
#         print(gretting, name)

# my_function('helo', 'hendrick','ronaldo','messi')

# Practical use of args 

# def my_function(*numebrs):
#     sum = 0
#     for number in numebrs:
#         sum += number
#     return sum

# print(my_function(10,20,30))


# def largest(*numbers):
#     max = numbers[0]

#     for number in numbers:
#         if number > max:
#             max = number
#     return max

# print(largest(2,9,8,10))


# def my_function(username, **details):
#   print("Username : " , username)
#   for key , value in details.items():
#     print(key + ":",value)

# my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

  
# def my_function(username, *args, **kwargs):
#     print(username)
#     print("Postional arguements :", args)
#     print("Keyword arguements :", kwargs)

# my_function("rakshyabhuju","jenny","menny","kenny",lastname = "bhuju", firstname = "Rakshya")


# def my_function(a, b, c):
#   return a + b + c
  
# numbers = [1, 2, 3]
# result = my_function(*numbers) 
# print(result)


# def my_function(**kwargs):
#   print("Hello", kwargs)

# person = {
#   "fname": "Emil", 
#   "lname": "Refsnes"
# }
# my_function(**person) 


# x = 300

# def myfunc():
#   x = 200
#   print(x)

# myfunc()

# print(x)

# def myfunc():
#   global x
#   x = 300

# myfunc()

# print(x)


# x = 'global'

# def outer():
#     x = 'enclosing'
#     def inner():
#         x = 'local'
#         print('Inner :', x)
#     inner()
#     print('Outer:', x)

# outer()
# print('Global :',x)







# def mainfunc(func):
#     def changecase():
#         return func().upper()
#     return changecase

# @mainfunc
# def myfunction(name):
#     return "K xa khabar haha!!" + name

# @mainfunc
# def otherfunction():
#     return "Haami ek nepali haau !!"

# print(myfunction('SHivan'))
# print(otherfunction())







# def mainfunc(n):
#     def innerfunc(val):
#         def func():
#             if n == 1:
#                 a = func().upper()
#             else:
#                 a = func().lower()
#             return a
#         return func
#     return innerfunc


# @mainfunc
# def func(num):
#     return "Hello World !!" + num

# print(func('namit'))







# def changecase(func):
#     def innerfunc():
#         return func().upper()
#     return innerfunc

# def grettingcase(func):
#     def innerfunc():
#         return "Good Morining " + func() + " jii !!"
#     return innerfunc

# @changecase
# @grettingcase
# def mainfunc():
#     return "Rakshya"

# print(mainfunc())






# def mainfunc(n):
#     def outermain(func):
#         def innermain():
#             if n == 1:
#                 a = func().lower()
#             else:
#                 a = func().title()
#             return a
#         return innermain
#     return outermain

# @mainfunc(0)
# def func():
#     return "Hey Hey BOYY !!"

# print(func())


# def myfunction():
#   return "Have a great day!"

# print(myfunction.__name__)



# LAMBDA EXPRESSIONS

# x = lambda z : z + 10
# print(x(5))

# y = lambda a , b , c : a * b * c
# print(y(1,2,3))


# def func(n):
#     return lambda b : b * n

# val = func(3)
# val1 = func(4)

# print(val(2))
# print(val1(10))


# List 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# odd_numbers = list(filter(lambda x : x % 2 == 0 , numbers))
# print(odd_numbers)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# new_num = list(map(lambda x : x * 2 , numbers))
# print(new_num)



# Recursion

# def myfunc(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * myfunc(n - 1)

# print(myfunc(10))
    
# def countdown(n):
#     if n <= 0:
#         print("COUNTDOWN")
#     else:
#         print(n)
#         countdown(n - 1)

# print(countdown(5))


# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(10))


# 0 1 1 2 3 

# def factorial(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(10))




# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
    
# print(fibonacci(7))


# Recursion with lists

# def sum_list(numbers):
#     if len(numbers) == 0:
#         return 0
#     else:
#         return numbers[0] + sum_list(numbers[1:])
    
# my_list = [1 , 2, 3 , 4 , 5]
# print(my_list[1:])
# print(sum_list(my_list))



# Python Generators

# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# for value in my_generator():
#     print(value)





