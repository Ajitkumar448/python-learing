# Build an Employee Profile Generator that takes in user input and creates a profile for an employee. The profile should include the employee's name, age, job title, and department. The program should also allow the user to input multiple employees and store their profiles in a list.
import string


First_name = input("Enter the employee's first name: ")
Last_name = input("Enter the employee's last name: ")
print(First_name )
print(Last_name)
full_name = First_name + " " + Last_name
print(full_name)
address = input("Enter the employee's address: ")
address += ", " + input("Enter the employee's city: ")
print(address)
employee_age = input("Enter the employee's age: ")
# Start by creating a variable employee_info and assign it the result of concatenating:

# the full_name variable

# a string consisting of the characters is preceded and followed by a space
# the employee_age variablemployee_info = full_name + " is " + employee_age + " years old."
employee_info = full_name + " is " + employee_age + " years old."
print(employee_info)
experience = input("Enter the employee's years of experience: ")
experience_info = full_name + " has " + experience + " years of experience."
position = input("Enter the employee's job title: ")
salary = input("Enter the employee's salary: ")
employee_card = f'employee: {full_name} | age: {employee_age} | experience: {experience} years | position: {position} | salary: ${salary}'
print(employee_card)
employee_code ="AJIT-2026-JD-001"
department = (employee_code [0:4])
print(department)
year_code = (employee_code[5:9])
print(year_code)
initials = (employee_code[10:12])
print(initials)
last_three = (employee_code[-3:])
print(last_three)