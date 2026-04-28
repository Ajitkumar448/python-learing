Total_bill = 0
Behavrage = float(input("Price of Behavrag:"))
Starter = float(input("Price of Starter:"))
Main_course= float(input("Price of main course:"))
Dessert = float(input("Price of Dessert:"))
Total_bill += Behavrage + Starter + Main_course + Dessert
print("Total bill is:",Total_bill)
Tip =float(input("tip is:"))
Total_bill += Tip
print("Total bill is:",Total_bill)
Frnds = int(input("no of friend:"))
Each_pay = Total_bill/Frnds
print("each frnd pay:",Each_pay)
Bill_per_person = round(Each_pay,1) 
print("Every frnd pays",Bill_per_person)
