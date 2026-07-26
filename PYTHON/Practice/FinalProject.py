# Employee Management System

"""
 Requirements:
 - Employee class (id, name, department, salary)
 - display() and update_salary() methods
 - Store employees in a list
 - Convert employee objects to dictionaries
 - Save and load data from employees.json
 - add_employee()
 - delete_employee()
 - search_employee()
 - Display all employees using loops
 - Handle invalid inputs using exception handling
"""


import json

class Employee:

    def __init__(self , id , name , department , salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary

    def update_salary(self , salary):
        self.salary = salary
        print('Salary updated Sucessfully.')

    def display(self):
         print('-' * 50)
         print(f' Employee ID    : {self.id} ')
         print(f' Employee Name     : {self.name} ')
         print(f' Employee Department   : {self.department}')
         print(f' Employee Salary   : {self.salary} ')

    def to_dict(self):
       return {
            'id' : self.id,
            'name' : self.name,
            'department' : self.department,
            'salary' : self.salary
        }
        

employees = []

# ------------------ Add Employee ------------------

def add_employee():
    try :
        emp_id  = int(input('Enter the ID of the user : '))
        name  = input('Enter the Name of the user : ')
        department  = input('Enter the department of the user : ')
        salary  = float(input('Enter the Salary of the user : '))

        for emp in employees:
            if emp.id == emp_id:
                print("Employee ID Already Exists.")
                return

        employee = Employee(emp_id, name , department , salary)
        employees.append(employee)

        print("Employee added sucessfully.")

    except ValueError:
        print('Invalid Input !! Employee ID must be integer , and salary must be numeric.')
    

# ------------------ Display ------------------

def display_all():
    if not employees:
        print('No employees Found.')
        return

    for emp in employees:
        emp.display()


# ------------------ Search ------------------

def search_employee():
    name = input('Enter the name :')

    found = False

    for emp in employees:
        if emp.name.lower() == name.lower():
            emp.display()
            found = True

    if not found:
        print('Employee not Found.')


# ------------------ Delete ------------------

def delete_employee():
    try:
        id = int(input('Enter the ID of the user you want to delete : '))

        for emp in employees:
            if emp.id == id:
                employees.remove(emp)
                print('Employee deleted sucessfully.')
                return

        print('Employee Not Found')

    except ValueError:
        print('Invalid ID.')


# ------------------ Update Salary ------------------

def update_salary():
    try:
        emp_id = int(input("Enter the ID of the employee to update the salary : "))

        for emp in employees:
            if emp.id == emp_id:
                salary = float(input("Enter the salary of the employee : "))
                emp.update_salary(salary)
                return

        print('Employee Not Found.')

    except ValueError:
        print('Invalid Input.')


# ------------------ Save JSON -----------------------

def save_to_json():
    data = []

    for emp in employees:
        data.append(emp.to_dict())

    try:
        with open('employees.json','w') as file:
            # Take this Python data and write it into the file as JSON.
            json.dump(data , file , indent=4)

        print('Employees saved sucessfully.')

    except Exception as e:
        print('Error while saving:', e)   

# ------------------ Load JSON ------------------

def load_from_json():
    try:
        with open('employees.json','r') as file:
            data = json.load(file)

        employees.clear()

        for emp in data:
            employee = Employee(
                emp['id'],
                emp['name'],
                emp['department'],
                emp['salary'],
            )

            employees.append(employee)

        print('Employees loaded sucessfully.')
 
    except FileNotFoundError:
        print("employees.json file not found.")

    except json.JSONDecodeError:
        print("Invalid JSON file.")

    except Exception as e:
        print("Error:", e)



# ------------------ Sample Data ------------------

employees.append(Employee(1, "Rehana", "IT", 20000))
employees.append(Employee(2, "Vihanu", "Marketing", 80000))
employees.append(Employee(3, "Sarthak", "Accounting", 250000))


# ------------------ Menu --------------------------


while True:
    print("\n========== Employee Management System ==========")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Update Salary")
    print("6. Save to JSON")
    print("7. Load from JSON")
    print("8. Exit")


    choice = input("Enter your choice: ")

    if choice == '1':
        add_employee()

    elif choice == '2':
        display_all()

    elif choice == '3':
        search_employee()

    elif choice == '4':
        delete_employee()

    elif choice == '5':
        update_salary()

    elif choice == '6':
        save_to_json()

    elif choice == '7':
        load_from_json()

    elif choice == '8':
        print('Goodbye !!')
        break

    else:
        print('Invalid Choice !!')







