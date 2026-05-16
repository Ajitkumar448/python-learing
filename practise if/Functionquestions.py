# def greet(): # Q 1 - to define a function that prints a greeting message
#     print("Hello, welcome to Python programming!")
# greet() # Q 1 - to call the greet function

# def my_name(): # Q 2 - to define a function that prints your name
#     print("My name is Ajit.")
# my_name() # Q 2 - to call the my_name function

# def sum(a,b): # Q 3 - to define a function that takes two parameters and returns their sum
#     return a+b
# result = sum(5,6) # Q 3 - to call the sum function with arguments 5 and 6 and store the result in a variable
# print(result) # Q 3 - to print the result of the sum function

# def square(): # Q 4 - to define a function that takes a number as input and returns its square
#     num = int(input("Enter a number: ")) # Q 4 - to take user input for the number
#     return num**2 # Q 4 - to return the square of the number
# return_value = square() # Q 4 - to call the square function and store the return value in a variable
# print(return_value) # Q 4 - to print the return value of the square function

# def square(a):
#     return a**2
# Square = square(4) # Q 5 - to call the square function with argument 4 and store the result in a variable named square
# print(Square) # Q 5 - to print the value of the variable square

# def cube(a): # Q 6 - to define a function that takes a number as input and returns its cube
#     return a**3
# Cube = cube(3) # Q 6 - to call the cube function with argument 3 and store the result in a variable named cube
# print(Cube) # Q 6 - to print the value of the variable cube

# def check(a):
#     if a%2==0: # Q 7 - to check if the number is even
#         return "Even" # Q 7 - to return "Even" if the number is even
#     else:
#         return "Odd" # Q 7 - to return "Odd" if the number is odd
# result = check(5)
# print(result) # Q 7 - to print the result of the check function with argument 5

# def largest(a,b):
#     if a>b: # Q 8 - to check if a is greater than b
#         return a # Q 8 - to return a if it is greater than b
#     else:
#         return b # Q 8 - to return b if it is greater than or equal to a
# result = largest(2,4)
# print(result) # Q 8 - to print the result of the largest function with arguments 5 and 4

# def smallest(a,b,c):
#     if a<b and a<c: # Q 9 - to check if a is the smallest among a, b and c
#         return a # Q 9 - to return a if it is the smallest
#     elif b<a and b<c: # Q 9 - to check if b is the smallest among a, b and c
#         return b # Q 9 - to return b if it is the smallest
#     else:
#         return c # Q 9 - to return c if it is the smallest
# result = smallest(3,1,2)
# print(result) # Q 9 - to print the result of the smallest function with arguments

# def greet(name):
#     return "hello, " + name
# result = greet("Ajit")
# print(result) # Q 10 - to call the greet function with argument "Ajit" and print the result

# def circle_area(radius):# Q 11 - to define a function that takes the radius of a circle as input and returns its area
#     area = 3.14 * radius**2
#     return area
# result = circle_area(7) # Q 11 - to call the circle_area function with argument 7 and store the result in a variable
# print(result) # Q 11 - to call the circle_area function with argument 7 and print the result    

# def area_rectangle(l,b): # Q 12 - to define a function that takes the length and breadth of a rectangle as input and returns its area
#     area = l*b
#     return area
# result = area_rectangle(5,3) # Q 12 - to call the area_rectangle function with arguments 5 and 3 and store the result in a variable
# print(result) # Q 12 - to print the result of the area_rectangle function with arguments

# def check(a):
#     if a>0: # Q 13 - to check if the number is positive
#         return "Positive" # Q 13 - to return "Positive" if the number is positive
#     elif a<0: # Q 13 - to check if the number is negative
#         return "Negative" # Q 13 - to return "Negative" if the number is negative
#     else:
#         return "Zero" # Q 13 - to return "Zero" if the number is zero
# result = check(5)
# print(result) # Q 13 - to print the result of the check function with argument 5

# def factorial(a):
#     fact = 1
#     for i in range(a,0,-1): # Q 14 - to calculate the factorial of a number using a for loop
#         fact *= i
#     return fact
# result = factorial(5) # Q 14 - to call the factorial function with argument 5 and store the result in a variable
# print(result) # Q 14 - to print the result of the factorial function with argument 5    

# def count_length(s):
#     count = 0
#     for char in s: # Q 15 - to count the number of characters in a string using a for loop
#         count += 1
#     return count
# result = count_length("ajit")
# print(result) # Q 15 - to call the count_length function with argument "ajit" and print the result

# def reverse(a):# Q 16 - to define a function that takes a string as input and returns its reverse
#     return a[::-1] # Q 16 - to return the reverse of the string using slicing
# result = reverse("ajit")
# print(result) # Q 16 - to call the reverse function with argument "ajit" and print the result

# def count_vowel(s):
#     count = 0
#     for char in s:
#         if char.lower() in "aeiou": # Q 17 - to check if the character is a vowel
#             count += 1 # Q 17 - to increment the count if the character is a vowel
#     return count
# result = count_vowel("ajit")
# print(result) # Q 17 - to call the count_vowel function with argument "ajit" and print the result

# def check_prime(a,):
#     for n in (range(2,a)):
#         if a%n==0:
#             return "Not prime"
#         else:
#             return "Prime"
# result = check_prime(7)
# print(result) # Q 18 - to call the check_prime function with argument 7 and print the result

# def find_sum (a): # Q 19 - to define a function that takes a list of numbers as input and returns their sum    
#     sum=0
#     for num in a: # Q 19 - to calculate the sum of a list of numbers using a for loop
#         sum+= num
#     return sum
# result = find_sum([1,2,3,4,5]) # Q 19 - to call the find_sum function with a list of numbers and store the result in a variable
# print(result) # Q 19 - to print the result of the find_sum function with a list of numbers

# def gmean(a,b): # Q 20 - to define a function that takes two numbers as input and returns their geometric mean
#     gmean = (a*b)/(a+b)
#     print(gmean)
# def Isgreater(a,b):
#     if a>b:
#         print("first is greater than b")
#     elif b>a:
#         print("second is greater than first")
#     else:
#         print("first and second are equal")
# def Isless(a,b):
#     pass
# a = 10
# b =10
# Isgreater(a,b) # Q 20 - to call the Isgreater function with arguments a and b and print the result
# gmean(a,b) # Q 20 - to call the gmean function with arguments a and b and print the result
# c= 20
# d=20
# Isgreater(c,d) # Q 20 - to call the Isgreater function with arguments c and d and print the result
# gmean(c,d) # Q 20 - to call the gmean function with arguments c and d and print the result

def sum(a=5,b=10): # Q 21 - default arguments takes two numbers as input and returns their sum with default values
    return a+b
result = sum() # Q 21 - to call the sum function without arguments and store the result in a variable
print(result) # Q 21 - to print the result of the sum function with default values

def sum(a,b=10): # Q 22 - to define a function that takes two numbers as input and returns their sum with one default value
    return a+b  
result = sum(5) # Q 22 - to call the sum function with one argument and store the result in a variable
print(result) # Q 22 - to print the result of the sum function with one default
def sum(a=5,b=10): # Q 23 - to define a function that takes two numbers as input and returns their sum with both default values
    return a+b
result = sum(b=5,a=20) # Q 23 - to call the sum function with both default values and store the result in a variable
print(result) # Q 23 - to print the result of the sum function with both default values

def avr(*num):# Q 24 - to define a function as tuples takes a variable number of arguments and returns their average
    sum=0
    for n in num:
        sum+=n
    return sum/len(num) # Q 24 - to define a function that takes a variable number of arguments and returns their average
result = avr(1,2,3,4,5) # Q 24 - to call the avr function with a variable number of arguments and store the result in a variable
print(result) # Q 24 - to print the result of the avr function with a variable

def name(**name):# Q 25 to define function as dictionary that takes a variable number of keyword arguments and returns a greeting message
    return "hello, " + name["fname"] + " " + name['mname'] + " " + name['lname'] # Q 25 - to define a function that takes a variable number of keyword arguments and returns a greeting message
# Q 25 - to print the result of the name function with a variable
print(name(fname="ajit", mname="kumar", lname="chauhan")) # Q 25 - to call the name function with a variable number of keyword arguments and print the result
