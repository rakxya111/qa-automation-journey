###### File AND Exception Handling


"""
1. Easy — Read a Test Report File

A text file named test_results.txt contains one test result on each line.

Write a program that:

Opens the file.
Reads all the lines.
Prints each test result.

Use proper exception handling in case the file does not exist.
"""


# try :
#     with open('D:/PYTHON/PYTHON/Practice/test_results.txt','r') as file:
#         data = file.read()
#         print(data)

# except FileNotFoundError:
#     print('File doesnot Exits.')

# finally:
#     print("The code is executed.")



"""
2. Easy — Save a Bug Report

Write a program that asks the user to enter a bug title.

Save the bug title to a file named bug_report.txt.

Use exception handling so the program handles any file writing error gracefully.
"""

# try:

#     title = input("Enter a Bug Title :")
#     with open('D:/PYTHON/PYTHON/Practice/test_results.txt','w') as file:
#         data = file.write(title)

        
# except FileNotFoundError:
#     print('File doesnot Exists.')






