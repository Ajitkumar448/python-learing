

# n= int(input("enter a number: "))
# def natural(n):
#  if n==0:
#     return
#  print(n)
#  natural(n-1)

# natural(n)

# n= int(input("enter a number: "))
# def sum_to_n(n):  # sum of first n natural numbers
#   sum =0
#   for i in  range(1,n+1):
#     sum+= i
    
#   return sum
# print(sum_to_n(n))

# # Recursive sum: no loop needed
# n= int(input("enter a number: "))
# def sum_to_n(n):
#     if n == 0:
#         return 0
#     return n + sum_to_n(n - 1)

# print(sum_to_n(n))  # 55

# def power(base,exponent):
#    result = base ** exponent
#    return result
# print(power(2,3))

# # Recursive power
# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent - 1)

# print(power(2, 3))  # 8

# def reverse(text):
#   reverse= text[::-1]
#   print (reverse)
# reverse("ajit")

# def reverse(text):
#     if text == "":
#         return ""

#     return text[-1] + reverse(text[:-1])

# print(reverse("ajit"))

# count= 1
# def printer(name):
#    global count
#    if count<=10:
#       print(name)
#       count+=1
#       printer(name)

# printer("ajit")

# def prime(n,i):# recursive function to check if a number is prime
#     if i==1:
#         return 1
#     if n%i==0:
#         return 0
#     return prime(n,i-1)
# n =int(input("enter a number: "))
# ind= prime(n,n-1)
# if ind==1:
#     print("prime number")
# if ind==0:
#     print("not a prime number")
   

# def prime(n): #simple function to check if a number is prime
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# num = int(input("enter a number: "))

# if prime(num):
#     print("prime number")
# else:
#     print("not a prime number")

# def sum_digit(n):
    
#     if n==0:
#        return 0
#     return n%10 + sum_digit(n//10)
# n = int(input("enter a num: "))
# print(sum_digit(n))

# def count_digit(n):
#     if n==0:
#         return 0
#     return 1 + count_digit(n//10)
# n = int(input("enter a num: "))
# print(count_digit(n))

# def fibonacci(n):
#     if n ==1:
#         return 0
#     if n ==2:
#         return 1
#     return (fibonacci(n-1)+ fibonacci(n-2))
# n= int(input("enter a number: "))
# for i in range(1, n + 1):
#     print(fibonacci(i), end=" ")

#     #LAMBDA FUNCTION

# X= lambda a,b: a+b
# print(X(5,6))

# X= lambda a:a**2
# print(X(5))

a = [1, 2, 3, 4, 5]
def func(a):
    if a%2==0:
        return True
    else:
        return False
def filter_even_numbers(a):
    return a*a
values = list(filter(func, a))
print(values)
squares = list(map(filter_even_numbers, values))
print(squares)

a = [1, 2, 3, 4, 5]
values = list(filter(lambda x: x % 2 == 0, a))
print(values)
squares = list(map(lambda x: x * x, values))
print(squares) 

ages =[10,15,20,42]

def adult(x):
    if x>=18:
        return True
    else:
        return False
    
adults = list(filter(adult, ages))
print(adults)

ages =[10,15,20,42]
adults = list(filter(lambda x: x >= 18, ages))  
print(adults)