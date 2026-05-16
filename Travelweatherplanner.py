distance_mi = int (input("enter distance"))
is_raining = input("enter whether its raining or not?(yes/no)")
has_bike = input("Have bike or not?(yes/no)")
has_car = input ("Have car or not?(yes/no)")
has_ridr_share_app = input("have ride share app or not(yes/no)")
if not distance_mi:
    print("distance is required")
elif 6 >= distance_mi >= 2:
    if is_raining == "no" and has_bike == "yes":
        print("you can use bike")
    else:
        print("you cannot go")
elif distance_mi > 6:
    if has_car == "yes" or has_ridr_share_app == "yes":
        print("you can use car or ride share")
    else:
        print("no suitable transportation method found")
