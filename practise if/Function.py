def sum (a,b):# to define a function that takes two parameters a and b
    return a+b

my_sum= sum(10,20)
print(my_sum)
def func():# to define a function that prints the value of my_var
    my_var = 10
    print(my_var)
func()
def outer_func():# to define an outer function that contains a nested inner function
    msg = "hii" 
    res =""
    def inner_func():
       nonlocal res
       res = "hello"
       print(msg)
    inner_func() 
    print(res)  
outer_func()
my_var =100
def func():# to define a function that modifies the global variable my_var
    global my_var
    my_var = 200
    print(my_var)
func()
print(my_var)
my_var_1 = 10
def ver():# to define a function that initializes a global variable my_var_2
    global my_var_2
    my_var_2 =20
    print(my_var_1 )
    print(my_var_2)
ver()
print(my_var_2)
def apply_discount(price, discount):# to define a function that applies a discount to a price
    if not isinstance(price, (int, float)):
        return "Error: Price must be a number."
    if not isinstance(discount, (int, float)):
        return "Error: Discount must be a number."
    if price < 0:
        return "Error: Price cannot be negative."
    if discount < 0 or discount > 100:
        return "Error: Discount must be in between 0 and 100."
    final_price = price -(price*discount/100)  
    return final_price
print(apply_discount(100,20))
print(apply_discount(50.5,10.5))
print(apply_discount(100,100))
print(apply_discount(100,0))
print(apply_discount(-50,10))
print(apply_discount(100,-10))   

