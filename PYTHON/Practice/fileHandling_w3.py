########## FILE HANDLING ##########


##### Read Mode in File Hanlding


# file = open('D:/PYTHON/PYTHON/Practice/new.txt', 'r')
# data = file.read()

# print(data)

# file.close()



##### Write mode in file handling -> Creates new file if it doesnot exists


# file = open('D:/PYTHON/PYTHON/Practice/new1.txt', 'w')

# data = input('What do you want to write on a file : ')

# file.write(data)

# print("data written sucessfully..")

# file.close()



#### Not to write the close everytime


# with open('D:/PYTHON/PYTHON/Practice/new1.txt', 'w') as file:
#     content = input("Say something : ")
#     file.write(content)
#     print("Written sucessfully !!!")


#### Append Mode in File Handling

# with open('D:/PYTHON/PYTHON/Practice/new1.txt', 'a') as file:
#     content = input("Say something : ")
#     file.write(content)
#     print("Written sucessfully !!!")



###### Readlines and import Os 

# import os

# if os.path.exists('D:/PYTHON/PYTHON/Practice/new1.txt'):
#     with open('D:/PYTHON/PYTHON/Practice/new1.txt') as f:
#        lines = f.readlines()
#        print(len(lines))
# else:
#     print('File doesnot Exists at all.')


