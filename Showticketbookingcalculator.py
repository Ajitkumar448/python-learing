Base_price =int(input("Enter the base price of the ticket: "))
Seat_type = input("Enter the seat type : ")
Showtime = input("Enter the showtime : ")
age = int(input("Enter the age of the person: "))
if age < 18:
    print("not eligible for booking ticket")
if age >= 21:
    print("user is eligible for booking evening show")
else:
    print("user is not eligible for booking evening show")
Service_charge = 0
if Seat_type == "premium":
    Service_charge = 50
    print("service charge for premium is:",Service_charge)
elif Seat_type == "Gold":
   Service_charge = 30  
   print("service for gold is:" ,Service_charge)
else :
    Service_charge = 0
    print("service charges:",Service_charge)
is_membership =input("Is user have membership?(yes/no): ")                                                                                                                                
is_weekend = input("Is it a weekend? (yes/no): ")
discount = 0
if is_membership and age >= 21:
    discount = 20
    print("user is eligible for discount")
else:    print("user is not eligible for discount")
print("Discount is:",discount)
extra_charge = 0
if is_weekend:
    extra_charge = 20
    print("extra charge is applied")
else:
    print("no extra charge applied")
print("extra charges is:",extra_charge)

if age >=21 or age >=18 and (Showtime!="evening" or is_membership):
    print("Eligible for ticket booking")
else:
   print("not eligible for ticket booking")
final_price = Base_price + extra_charge + Service_charge - discount
print("ticket price is:",final_price)
