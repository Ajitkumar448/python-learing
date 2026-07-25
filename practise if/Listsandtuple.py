cities =["DELHI","PATNA","AGRA","NOIDA"]
print(cities)
print(cities[0]) # Q 1 - to print the first element of the list cities
name ="ajit"
print(list(name)) # Q 2 - to print the list name
num =[1,2,3]
num.extend([4,5,6]) # Q 3 - to append the numbers 4,5,6 to the list num
del num[0]
print(num) # Q 3 - to print the list num after deleting the first element
print(num[1:6:2]) # Q 3 - to print the elements of the list num from index 1 to 5 with a step of 2
profile=["ajit","mca","final"]
profile.insert(3, "delhi") # Q 4 - to insert the string "delhi" at index 3 of the profile list
name,subject,year,city = profile
print(name) # Q 4 - to print the name variable after unpacking the profile list
print(subject) # Q 4 - to print the subject variable after unpacking the profile list
print(year) # Q 4 - to print the year variable after unpacking the profile list
print(city) # Q 4 - to print the city variable after unpacking the profile list
name,*rest = profile
print(name) # Q 5 - to print the name variable after unpacking the profile list with rest
print(rest) # Q 5 - to print the rest variable after unpacking the profile list
nums =[2,5,5,8,3,1,4]
nums.remove(5) # Q 6 - to remove the first occurrence of the number 5 from the nums list
print(nums) # Q 6 - to print the nums list after removing the first occurrence of
nums.sort() # Q 7 - to sort the nums list in ascending order
print(nums) # Q 7 - to print the nums list after sorting in ascending order
nums.sort(reverse=True) # Q 7 - to sort the nums list in descending order
print(nums) # Q 7 - to print the nums list after sorting in descending order
nums.index(3) # Q 8 - to find the index of the first occurrence of the number 3 in the nums list
print(nums.index(3)) # Q 8 - to print the index of the first occurrence
print(nums.count(5)) # Q 9 - to count the number of occurrences of the number 5 in the nums list    

words =["python","java","c++","ruby"]
for word in words:
    for letter in word:
        if letter.lower() in "aeiou":
            print(f'{word} has a vowel in it: {letter}') 
            break
    else:
        print(f"{word} has no vowels.") # Q 10 - to print the vowels in each word of the words list
tup= ("ak",2,"ind"  ) # Q 11 - to create a tuple with the elements "ak", 2, and "ind"
print(tup) # Q 11 - to print the tuple tup

nm ="ajit"
print(tuple(nm)) # Q 12 - to convert the string nm into a tuple and print it


categories =("fruits","vegetables") # Q 13 - to create a tuple named categories with the elements "fruits", "vegetables", and "dairy"
food =("apple","carrot","kiwi") # Q 13 - to create a tuple named food with the elements "apple", "carrot", and "kiwi"
for category in categories:
    for item in food:
        print(f"{item} is a {category}") # Q 13 - to print each item in the food tuple along with its corresponding category from the categories tuple

secnum=7
guess =0
while guess != secnum:# Q 14 - to show while loops run until value becomes false
    guess = int(input("Enter your guess (1-10): "))
    if guess!= secnum:
        print("Wrong guess, try again!")
print("Congratulations! You guessed the secret number.") # Q 14 - to create a simple guessing game where the user has to guess a secret number and receives feedback on whether their guess is correct or not

Name = ["ajit","anil","arun","amit"] # Q 15 - use of break to stop loop when a certain condition is met
for name in Name:
 if name == "arun":
       break
 print(name)
Name = ["ajit","anil","arun","amit"] # Q 15 - use of break to stop loop when a certain condition is met
for name in Name:
 if name =="anil":
   continue
 print(name) # Q 15 - to demonstrate the use of break and continue statements in a loop by iterating through a list of names and breaking the loop when a specific name is encountered, and using continue to skip a specific name while printing the others

#RANGE
for i in range(5): # Q 16 - to demonstrate the use of the range function in a for loop by iterating through a sequence of numbers from 0 to 4 and printing each numb
    print(i)
for i in range(1, 10, 2): # Q 16 - to demonstrate the use of the range function in a for loop by iterating through a sequence of numbers from 1 to 9 with a step of 2 and printing each number
    print(i ,end=" ")
print("all is odd numbers")
for i in range(1,10,2): # Q 16 - to demonstrate the use of the range function in a for loop by iterating through a sequence of numbers from 1 to 9 with a step of 2 and printing each number
    if i in (3,5,7):
        print(f"{i} is a prime number")

#Enumerate
fruits = ["apple", "banana", "cherry"] # Q 17 - to demonstrate the use of the enumerate function in a for loop by iterating through a list of fruits and printing both the index and the fruit name for each item in the list
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
list(enumerate(fruits)) # Q 17 - to convert the enumerate object into a list and print it
print(list(enumerate(fruits))) # Q 17 - to print the list of tuples generated by the enumerate function, where each tuple contains the index and the corresponding fruit name from the fruits list

languages = ["python", "java", "c++"] # Q 18 - to demonstrate the use of the enumerate function in a for loop by iterating through a list of programming languages and printing both the index and the language name for each item in the list
for index, language in enumerate(languages,1):
    print(f"Index: {index}, Language: {language}") # Q 18 - to demonstrate the use of the enumerate function in a for loop by iterating through a list of programming languages and printing both the index and the language name for each item in the list, starting the index from 1 instead of 0 

#ZIP
names = ["Alice", "Bob", "Charlie"] # Q 19 - to demonstrate the use of the zip function by creating two lists, one with names and another with ages, and then using zip to combine them into a list of tuples where each tuple contains a name and its corresponding age
ages = [25, 30, 35]
zipped = zip(names, ages)
print(list(zipped)) # Q 19 - to convert the zip object into a list and print it, showing the combined list of tuples with names and ages
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.") # Q 19 - to iterate through the zipped lists of names and ages and print a formatted string for each name and its corresponding age

#List comprehension
numbers = [1, 2, 3, 4, 5] # Q 20 - to demonstrate the use of list comprehension by creating a new list that contains the squares of the numbers from an existing list of numbers
result =[(num,"even") if num % 2 == 0 else (num,"odd") for num in numbers] # Q 20 - to create a new list of tuples using list comprehension, where each tuple contains a number from the original list and a string indicating whether the number is "even" or "odd"
print(result) # Q 20 - to print the new list of tuples generated by the list

words =["hello","world","python","dart"] # Q 21 - to demonstrate the use of list comprehension by creating a new list that contains the lengths of each word from an existing list of word
def long_word(word):
    return len(word) > 5
result = list(filter(long_word, words)) # Q 21 - to create a new list using the filter function and a custom function that checks if the length of each word is greater than 5, resulting in a list of long words from the original list
print(result) # Q 21 - to print the new list of long words generated by thefilter function, showing only the words from the original list that have a length greater than 5
 
#Map
celsius = [0, 10, 20, 30] # Q 22 - to demonstrate the use of the map function by creating a new list that contains the Fahrenheit equivalents of a list of temperatures in Celsius
def celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32
result = list(map(celsius_to_fahrenheit, celsius)) # Q 22 - to create a new list using the map function and a custom function that converts each temperature from Celsius to Fahrenheit
print(result) # Q 22 - to print the new list of temperatures in Fahrenheit generated by the map function, showing the converted values from the original list of Celsius temperatures

nums= [1, 2, 3, 4, 5] # Q 23 - to demonstrate the use of the map function by creating a new list that contains the squares of each number from an existing list of numbers
total =sum(nums,10)
print(total) # Q 23 - to calculate and print the sum of all the numbers in the original list using the sum function, showing the total of the numbers in the list

#lambda
 #give a program to add 5 user entered fruits n ame in a list
fruits = []

for i in range(5):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)

print("Fruit List:", fruits)

marks =[]
for i in range(6):
    mark=int(input(f"enter marks {i+1}: "))
    marks.append(mark)
    marks.sort()
print("marks sorted list:" ,marks)

num = [23,54,12,43]
sum = 0
for n in num:
    sum+=n
print(sum)

a=(1,0,0,2,3)
print(a.count(0))