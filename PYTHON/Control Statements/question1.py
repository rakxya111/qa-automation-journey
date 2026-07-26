## 1. Even or odd.

# print("Check Even or Odd")
# val = int(input("Enter any number : "))

# if(val % 2 == 0):
#     print(f'{val} is even number')
# else:
#     print(f'{val} is odd number')


##  2. Pass or fail.


# val = int(input("Enter the marks in the subject : "))
# if(val <=35):
#     print("You failed.")
# else:
#     print("You passed")


##  3. Positive, negative or zero.

# val = int(input("Enter the number :"))
# if(val >= 1):
#     print("The number is postive.")
# elif(val == 0):
#     print("The number is zero")
# else:
#     print("The number is negative")



##  4. Largest among three numbers.

# val = int(input("Enter number 1 : "))
# val1 = int(input("Enter number 2 : "))
# val2 = int(input("Enter number 3 : "))

# if((val > val1) and (val > val2)):
#     print(f'{val} is the greatest.')
# elif((val1 > val) and (val1 > val2)):
#     print(f'{val1} is the greatest.')
# else:
#     print(f'{val2} is the greatest.')



#  6. Loops
# - for, while, break, continue
 

#  1. Print 1–100.

# i = 1
# while (i <= 100):
#     print(i)


# for i in range(1,101):
#     print(i)

# start = int(input("Enter starting number : "))
# end = int(input("Enter the end number : "))
# skip = int(input("Enter the number you want to skip : "))

# if(start < end ):
#     for i in range(start, end):
#         if i == skip:
#             continue
#         else:
#             print(i)
# else:
#     print("The starting number should be greater than end number.")
        


#  2. Print even numbers.

# for x in range(1,100):
#     if x % 2 == 0:
#         print(x)
    

#  3. Multiplication table.

# for x in range(1,11):
#     for y in range(1,11):
#         print(f' {x} * {y} = {x * y }')


#  4. Sum of first 50 numbers.

# sum = 0
# for i in range(1,51):
#     sum += i

# print(sum)


# fruits = ['apple' , 'banana', 'coconut']

# for x in fruits:
#     if x == 'banana':
#         break
#     print(x)


# for x in "fruits":
#     print(x)


# for x in range(6):
#    if x == 3: break
#    print(x) 
# else:
#     print("Finally !!!")


