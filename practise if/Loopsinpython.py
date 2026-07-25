name = "ajit" #1 example of loops in string
for c in name:
 print(c)
 if c=='a':
  print("A for Ajit")
Fruits = ["apple","banana","grapes"] #2 example of loops in list
for f in Fruits:
    print(f)
    if f=="banana":
     print("I like banana")
for i in range(1,100): #3 example of loops in range
    print(i)
    if i%2==0:
     print("Even")
    else:
     print("Odd")
for i in range(1,100,2): #4 example of loops in range with step
    print(i ,end=" ") # to print the numbers in the same line with a space in between
print("all odd numbers from 1 to 100") # to print a message after the loop is finished

while True: #5 example of while loop to create a simple calculator menu
    print("Menu")
    print("1.add")
    print("2.subs")
    print("3.mul")
    print("4.div")
    print("5.exit")
    choice = int(input("enter your choice: "))
    if choice==5:
      print("Exiting...")
      break
    a = int(input("enter a number: "))
    b = int(input("enter another numbe: "))
    if choice==1:
     print(a+b)
    elif choice==2:
     print(a-b)
    elif choice==3:
     print(a*b)
    elif choice==4:
     print(a/b)
    else:
      print("Invalid input")
      


    
