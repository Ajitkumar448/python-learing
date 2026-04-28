My_string = "  Hello, World!  "
a = '''ajit is a student'''
b = ' it\'s spring season '
a = "ajit"
b = "24"
c = f'My name is {a} and I am {b} years old.'
d =str(input("enter a name"))
e = 'good morning'
print("good morning",+'a')
a_plus_b = a + b #string concatenation
# [0] = "A" strings are immutable, this will raise an error
print(My_string)
print(len(My_string)) #length of the string
print(My_string[0]) #first character
print(My_string[-1]) #last character
print(My_string[0:2]) #substring from index 0 to 4 
print(My_string[-4:-2]) #substring from index -4 to -3  
print(My_string[:13]) #substring from index 0 to 12
print(My_string[7:]) #substring from index 7 to the end
print(My_string[1:13:3]) #substring from index 1 to 12 with a step of 3
print(a.endswith("t")) #check if the string ends with "t"
print(a.startswith("a")) #check if the string starts with "a"
print(My_string.count("o")) #count the number of occurrences of "o"
print(My_string.find("o")) #find the index of the first occurrence of "o"
print(a.capitalize()) #capitalize the first letter of the string
print(My_string.replace("o", "0")) #replace all occurrences of "o" with "0"
print(b)
print("spring" in b) #check if "spring" is in the string b
print("summer" in b) #check if "summer" is in the string b
print(a)
print(a_plus_b)
print(c)
print(a.upper()) #convert the string to uppercase
print(a.lower()) #convert the string to lowercase
print(My_string.strip()) #remove leading and trailing whitespace
print(My_string.replace("!", "$")) #replace " !" with "$" in the string My_string
print(My_string.split(",")) #split the string My_string into a list using "," as the delimiter
print(a.isalpha()) #check if the string a contains only alphabetic characters
print(b.isdigit()) #check if the string b contains only digits
print(a.isalnum()) #check if the string a contains only alphanumeric characters
print(b.isalnum()) #check if the string b contains only alphanumeric characters
print(a.startswith("a")) #check if the string a starts with "a"
print(a.find("j")) #find the index of the first occurrence of "j" in the string a
print(c.capitalize()) #capitalize the first letter of the string c
print(c.title()) #capitalize the first letter of each word in the string c
print("good morning " + d ) #print "good morning" followed by the value of d
print( e.title() + " " + d ) # Q1 -capitalize the first letter of each word in the string e and concatenate with d

Date = "24-06-2024"
letter ='''Dear {d},
you are selected !
{Date}'''
print(letter.format(d=d, Date=Date)) # Q2 - use the format method to replace the placeholders in the letter with the values of Name and Date
letter2 = f'''Dear {d},
you are selected !
{Date}'''
print(letter2) # Q3 - use an f-string to replace the placeholders in the letter with the values of Name and Date
# Q4 write a program to detect double spaces in a string
double_space_string = "This  is a string with double spaces."
if "  " in double_space_string: # check if there are double spaces in the string
    print("Double spaces detected.") 
else:
 print("No double spaces detected.")
    #  Q3 replace double spaces with single spaces
single_space_string = double_space_string.replace("  ", " ")
print(single_space_string)
letter3 = "Dear,Harry,this Python Course is amazing! thank you."
print(letter3.split(",")) # Q5 split the letter3 into a list using "," as the delimiter
    


# # Q4 write a program to detect double spaces in a string
double_space_string = "This  is a string with double spaces."
if "  " in double_space_string: # check if there are double spaces in the string
    print("Double spaces detected.") 
else:
    print("No double spaces detected.")
    #  Q3 replace double spaces with single spaces
    single_space_string = double_space_string.replace("  ", " ")
    print(single_space_string)
letter3 = "Dear,Harry,this Python Course is amazing! thank you."
#Q5 format the following letter using escape sequence characters
formatted_letter = "Dear Harry,\nThis Python Course is amazing!\nThank you."
print(formatted_letter)
    





