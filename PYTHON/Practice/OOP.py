"""
1. Easy — Create a Test Case Class

Create a class named TestCase with the following attributes:

test_id
title
status

Create two objects of the class with different values and print the details of each object.

"""
# Answer :

# class Testcase:
#     def __init__(self , test_id , title , status):
#         self.test_id = test_id
#         self.title = title
#         self.status = status
    
#     def print_detail(self):
#         print(self.test_id , self.title , self.status)

# t1 = Testcase(1, 'Checking authentication', 'Ongoing')
# t2 = Testcase(2, 'Validating buttons', 'Completed')

# t1.print_detail()
# t2.print_detail()



"""
2. Easy — Browser Class with a Method

Create a class named Browser with an attribute:

browser_name

Add a method named launch() that prints a message indicating that the browser has been launched.

Create objects for Chrome and Firefox and call the launch() method for both.
"""


# Answer :

# class Browser:
#     def __init__(self, browser_name):
#         self.browser_name = browser_name
    
#     def launched(self):
#         print(f'{self.browser_name} is launched.')

# o1 = Browser('Chrome')
# o1.launched()

# o2 = Browser('Firefox')
# o2.launched()



"""
3. Moderate — Test Suite Class

Create a class named TestSuite with:

an attribute suite_name
an attribute total_tests

Add the following methods:

add_test() → increases the total number of tests by 1.
show_summary() → displays the suite name and current total number of tests.

Create one object and call add_test() multiple times before displaying the summary.

"""

# Answer :

# class TestSuite:

#     def __init__(self, suite_name):
#         self.suite_name = suite_name
#         self.total_tests = 0
    
#     def add_test(self):
#        self.total_tests += 1
        

#     def show_summary(self):
#         print(f'Suite name: {self.suite_name} , Total Tests: {self.total_tests}')


# t1 = TestSuite('Login')
# t1.add_test()
# t1.add_test()
# t1.show_summary()



"""
4. Moderate — API Request Class with Constructor

Create a class named APIRequest whose constructor accepts:

endpoint
method

Add a method named send_request() that prints a message using the object's values.

Create at least three different API request objects and call the method for each.
"""

# Answer :

# class APIRequest:
#     def __init__(self , endpoint, method):
#         self.endpoint = endpoint
#         self.method = method
    
#     def send_request(self):
#         print(f'Sending {self.method} request to {self.endpoint}')

# a1 = APIRequest('/users', 'GET')
# a2 = APIRequest('/manager', 'POST')
# a3 = APIRequest('/student/3', 'PUT')
# a4 = APIRequest('/pos/users/1', 'PATCH')

# a1.send_request()
# a2.send_request()
# a3.send_request()
# a4.send_request()


"""
5. Moderate — Login Page Object

Create a class named LoginPage with attributes:

username
password

Add two methods:

enter_credentials()
click_login()

Create an object, assign suitable values, and call both methods in the correct order.
"""

# Answer :

# class LoginPage:
#     def __init__(self, username='', password=''):
#         self.username = username
#         self.password = password

#     def enter_credentials(self, username=None, password=None):
#         if username is None or password is None:
#             username = input('Enter username: ')
#             password = input('Enter password: ')
#         self.username = username
#         self.password = password

#     def click_login(self):
#         if self.username and self.password:
#             print(f'Logging in as {self.username}')
#         else:
#             print('Login failed: missing username or password')


# page = LoginPage()
# page.enter_credentials('alice', 's3cr3t')
# page.click_login()


"""
6. Slightly Challenging — Manage Multiple Test Cases

Create a class named TestCase with attributes:

test_id
title
status

Create at least four different TestCase objects and store them in a list.

Use a loop to display the details of every test case by accessing each object's attributes.
"""

# Answer :

# class Testcase:
#     def __init__(self, test_id, title, status):
#         self.test_id = test_id
#         self.title = title
#         self.status = status

#     def details(self):
#         print(f'{self.test_id} : {self.title} , {self.status}')


# t1 = Testcase(1,'Registration', 'Ongoing')
# t2 = Testcase(2,'Login', 'Completed')
# t3 = Testcase(3,'Student', 'Rejected')
# t4 = Testcase(4,'Teacher', 'In Hold')

# objects = [t1, t2, t3, t4]

# for k in objects:
#     k.details()


# ALL IN ONE QUESTIONS

"""
1. Easy — Inheritance

Create a class named TestCase with attributes:

test_id
title

Create another class named UITestCase that inherits from TestCase and adds a new attribute:

browser

Create an object of UITestCase and display all its information.
"""     

# Answer :

# class Testcase:
#     def __init__(self, test_id, title):
#         self.test_id = test_id
#         self.title = title
    
# class UITestcase(Testcase):
#     def __init__(self, test_id, title , browser):
#         super().__init__(test_id, title)
#         self.browser = browser
    
#     def display(self):
#         print(f'{self.test_id} : {self.title} , {self.browser}')

# u1 = UITestcase(1, 'Authentication', 'Chrome')
# u1.display()        



"""
2. Easy — Method Overriding

Create a class named Browser with a method named open().

Create two child classes:

Chrome
Firefox

Override the open() method in each child class so that each browser displays its own message.

Create one object of each child class and call the method.
"""

# Answer :

# class Browser:
#     def method(self):
#         pass

# class Chrome(Browser):
#     def method(self):
#         print("This is chrome browser.")

# class Firefox(Browser):
#     def method(self):
#         print("This is firefox browser.")

# a = Browser()
# b = Chrome()
# c = Firefox()

# a.method()
# b.method()
# c.method()


"""
3. Moderate — Polymorphism

Create the following classes:

Chrome
Firefox
Edge

Each class should contain a method named launch().

Store objects of all three classes in a list and use a single loop to call the launch() method on every object.
"""

# Answer :

# class Chrome:
#     def launch(self):
#         print("This is chrome.")

# class Firefox:
#     def launch(self):
#         print("This is firefox")

# class Edge:
#     def launch(self):
#         print("This is Edge")


# a = Chrome()
# b = Firefox()
# c = Edge()

# browsers = [a, b, c]

# for b in browsers:
#     b.launch()



"""
4. Moderate — Encapsulation

Create a class named LoginPage.

Store the password as a private attribute.

Provide:

one method to update the password
one method to display the username and password

Create an object, update the password using the provided method, and display the updated information.
"""

# Answer :

# class LoginPage:
#     def __init__(self , username , password):
#         self.username = username
#         self.__password = password
    
#     def update_password(self, new_password):
#         self.__password = new_password
    
#     def display_details(self):
#         return f'Username : {self.username} , Password : {self.__password} '
    
# ob = LoginPage('rakshyabhuju', 'r@123$')
# print(ob.display_details())

# ob.update_password('nhujioo')
# print(ob.display_details())
        




"""
5. Moderate — Using an Inner Class

Create a class named TestReport.

Inside it, create an inner class named Summary.

The inner class should store:

total tests
passed tests

Create objects of both classes and display the summary information.
"""
# Answer :

# class TestReport:
#     class Summary:
#         def __init__(self, total_tests, passed_tests):
#             self.total_tests = total_tests
#             self.passed_tests = passed_tests
            

# t1 = TestReport()
# t2 = t1.Summary(4 , 3)

# print(t2.total_tests)
# print(t2.passed_tests)



"""
6. Slightly Challenging — Multiple OOP Concepts

Create a base class named Employee with:

employee name
employee ID

Create two child classes:

ManualTester
AutomationTester

Each child class should override a method named work() with its own implementation.

Store objects of both child classes in a list and use a loop to:

display the employee details
call the work() method for each object
"""

# Answer :

# class Employee:
#     def __init__(self, emp_id, emp_name):
#         self.emp_id = emp_id
#         self.emp_name = emp_name
    
#     def employee_details(self):
#         print(f'{self.emp_id} , {self.emp_name}')

# class ManualTester(Employee):
#     def work(self):
#         print("This is manual Tester.")

# class AutomationTester(Employee):
#     def work(self):
#         print("This is automation Tester.")

        
# e1 = ManualTester(1, 'Ramesh')
# e2 = AutomationTester(2, 'Rakesh')

# employee = [e1 , e2]

# for emp in employee:
#     emp.employee_details()
#     emp.work()


