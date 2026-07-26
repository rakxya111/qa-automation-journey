
########### Exception Handling ##################


# try:
#     num = int(input("Enter a number : "))

#     result = 10 / num
#     print(f"The result is : {result}")

# except ZeroDivisionError:
#     print("You can't divide by zero.")

# except ValueError:
#     print("You can't divide by string.")




# try:
#     file = open('C:\Users\Acer\AppData\Local\Programs\Python\Python314', 'r')

# except FileNotFoundError:
#     print('File not found')

# finally:
#     file.close()
#     print('File operation is completed.')




####### Nested Try except

# try:
#     num1 = int(input("Enter a number : "))
#     num2 = int(input("Enter second number : "))

#     try:
#         divison = num1 / num2
#         print(f'Result is : {divison}')
    
#     except ZeroDivisionError:
#         print('Cannot be divided by zero')

# except ValueError:
#     print('Cannot be a string.')

# finally:
#     print("The code has been executed.")




######## Customized EXCEPTION HANDLING : Check password strength

# def check_password(password):
#     if len(password) < 8 :
#         raise Exception('Error : The password length must be greater than 8.')
#     print('Password is strong')

# try:
#     password = input('Enter the password : ')
#     check_password(password)
# except Exception as e:
#     print(e)


