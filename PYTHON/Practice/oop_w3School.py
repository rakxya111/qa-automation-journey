# OOP - Object Oriented Programming
"""
Data = attributes / Properties
Functions = Methods / Behaviour

Solves : Code Duplication

"""

# class Car:
#     def set_details(self,name ,colour):
#         self.name = name
#         self.colour = colour
    
#     def show_details(self):
#         print(f'The name of the car is {self.name} and the colour of the car is {self.colour}')


# car1 = Car()
# car1.set_details('Tesla','Black')
# car1.show_details()




##### Constructor


# class Car:

#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
    
#     def details(self):
#         print(f'The name of the car is {self.name} and the color is {self.color}.')

# obj1 = Car('Rolls Royce','Maroon')
# obj1.details()
# print(obj1.name)
# print(obj1.color)





#### There are default parameterized constructor , also can call the methods inside the class

# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     def greet(self):
#         return f'Hello {self.name}'
    
#     def welcome(self):
#         message = self.greet()
#         print(message + ', Welcome to our website.')

# p1 = Person('Rakshya')
# p1.welcome()



# Properties - : The properties are the variables that belong to the class , they 

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    

# car1 = Car('Toyota', 'Corolla')

# print(car1.brand)
# print(car1.model)

# # Modify the properties
# car1.model = 'rakshya'
# print(car1.model)

# # Delete the properties
# del car1.model



#  Class Properties :

# class Car:
#     color = ""
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    

# car1 = Car('Toyota', 'Corolla')
# car2 = Car('Hyundai', 'Motorolla')

# Car.color = "Red"

# print(car1.color)
# print(car2.color)

# car1.year = 1998

# print(car1.year)



# Methods

# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self):
#         return f'Hello my name is {self.name}'

# p1 = Person('Rakshya') 
# print(p1)



# class Playlist:
#     def __init__(self,name):
#         self.name = name
#         self.songs = []
    
#     def get_songs(self,song):
#         self.songs.append(song)
#         print(f'Added new song {song}')
    
#     def remove_songs(self,song):
#        if song in self.songs:
#            self.songs.remove(song)
#            print(f'Song removed {song}')
    
#     def show_songs(self):
#         print(f'Playlist {self.name}')
#         for song in self.songs:
#             print(f'-{song}')

# my_playlist = Playlist('Favorites')
# my_playlist.get_songs('Sayara')
# my_playlist.get_songs('Heart')
# my_playlist.show_songs()






# Inheritance

# class Person:
#     def __init__(self, fname , lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def printname(self):
#         print(self.firstname , self.lastname)

# class Student(Person):
#     pass

# x = Student("Raima","Hedger")
# x.printname()








#  Use of the parent class name to inherit the parent class methods and preoperties.

# class Person:
#     def __init__(self, fname , lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def printname(self):
#         print(self.firstname , self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self,fname, lname)

# x = Student("Raima","Hedger")
# x.printname()








# class Person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname
    
   
# class Student(Person):
#     def __init__(self,fname,lname,birthyear,graduation_date):
#         super().__init__(fname,lname)
#         self.birthyear = birthyear
#         self.graduation_date = graduation_date
    
#     def printdata(self):
#         print(self.firstname , self.lastname, self.birthyear, self.graduation_date)

    
# s1 = Student('Rakshya','Bhuju', 2003 , 2026)
# s1.printdata()
        







# Polymorphism
    
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("Drivee !!!")

# class Boat:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("Sail !!!")

# class Airplane:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("Flyy !!!")

# car1 = Car("Ford", "Mustang")       
# boat1 = Boat("Ibiza", "Touring 20") 
# plane1 = Airplane("Boeing", "747")  

# for x in (car1, boat1 , plane1):
#     x.move()
        







# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("MOVEE!")
    
# class Car(Vehicle):
#    pass

# class Boat(Car):
#     def move(self):
#         print('SAILL !!')

# class Plane(Car):
#     def move(self):
#         print('FLYY !!')

# car1 = Car("Ford", "Mustang")       
# boat1 = Boat("Ibiza", "Touring 20") 
# plane1 = Plane("Boeing", "747") 

# for x in (car1 , boat1 , plane1):
#     print(x.brand)
#     print(x.model)
#     x.move()
#     print(" ")






# Encapsulation

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
    
# p1 = Person('Rakshya' , 22)
# print(p1.name)
# print(p1.__age)






# GETTER

# class Person:
#     def __init__(self, name , age):
#         self.name = name
#         self.__age = age
    
#     def get_age(self):
#         return self.__age

# p1 = Person('Rakshya', 22)
# print(p1.get_age())





# SETTER

# class Person:
#     def __init__(self, name , age):
#         self.name = name
#         self.__age = age
        
#     def set_age(self, age):
#         if 0 <= age <= 100:
#             self.__age = age
#         else:
#             print("Age must be between 0 to 100.")
    
#     def get_age(self):
#         return self.__age
    
#     def get_status(self):
#         if self.__age > 100 or self.__age < 0:
#             print("NOT ELIGIBLE SORRY !!!!", end='')
#         else:
#             print("COngratulations !!!!!", end='')


# p1 = Person('Rakshya', 22)
# print(p1.get_age())
# p1.get_status()

# p1.set_age(19)
# print(p1.get_age())
# p1.get_status()

# p1.set_age(-10)
# print(p1.get_age())
# p1.get_status()






# Protected Properties

# class Person:
#   def __init__(self, name, salary):
#     self.name = name
#     self._salary = salary # Protected property

# p1 = Person("Linus", 50000)
# print(p1.name)
# print(p1._salary) # Can access, but shouldn't





# Private Methods

# class Calculator:
#     def __init__(self):
#         self.result = 0
    
#     def __validate(self, num):
#         if isinstance(num, (int , float)):
#             return True
#         return False
    
#     def add(self, num):
#         if self.__validate(num):
#             self.result += num
#         else:
#             print("Invalid Number")

# calc = Calculator()
# calc.add(10)
# calc.add(5)
# print(calc.result)







# Name Mangling

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
    
# p1 = Person("Emil", 30)

# print(p1._Person__age)






# PYTHON INNER CLASS

# class Outer:
#     def __init__(self):
#         self.name = 'Outer class'
    
#     class Inner:
#         def __init__(self):
#             self.name = 'Inner class'
        
#         def display(self):
#             print("This is inner class.")

# out = Outer()
# print(out.name)

# inn = out.Inner()
# print(inn.name)
# inn.display()





# Practical Example of Inner Class

# class Car:
#     def __init__(self , brand , model):
#         self.brand = brand
#         self.model = model
#         self.engine = self.Engine()
    
#     class Engine:
#         def __init__(self):
#             self.status = "Off"
        
#         def start(self):
#             self.status = 'Running'
#             print("Engine Started !!")
       
#         def stop(self):
#             self.status = 'Off'
#             print("Engine Stopped !!")
    
#     def drive(self):
#         if self.engine.status == "Running":
#             print(f'Driving the {self.brand} {self.model}')
#         else:
#             print('Start the engine first !!!')


# car = Car('Rolls Royce', '2002')
# car.drive()
# car.engine.start()
# car.drive()


