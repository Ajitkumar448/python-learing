def shopping_cart():
    items = {"apple": 30,
             "chips": 20,
            "chocolate": 50,
            "milk": 40
                      }
    total_price = 0
    while True:
     print("    Menu   ")
     print("1.add item")
     print("2.view cart")
     print("3.exit")
     choice = int(input("Enter your choice: "))
     if choice == 1:
        item = input("Enter the item name: ").lower()
        quantity = int(input("enter quantity: "))
        if item in items:
            total_price += items[item]* quantity
            print(f"{item} added to cart. Price: {items[item]}")
        else:
            print("Item not found in the menu.")
     elif choice == 2:
        print(f"Total price of items in cart: {total_price}")
     elif choice == 3:
        
        print("Exiting the shopping cart. Thank you for shopping!")
        break
        
     else:
        print("Invalid choice. Please try again.")
shopping_cart()


          
