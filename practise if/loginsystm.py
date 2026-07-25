def login_system():
   attempt = 0
   while attempt < 3:
     user =input("enter the user name:").lower()
     password= input("enter password: ")

     if user == "ajit" and password =="1234":
            print( "login successful")
            return
     else:
            attempt += 1
            print("invalid credential")
            
            print(f"attempt left : {3 - attempt}")
            
   print("account blocked")
     
(login_system())

def check_login(username, password):

    # Username validation
    if not isinstance(username, str) or len(username.strip()) == 0:
        return {
            "valid": False,
            "message": "Username cannot be empty"
        }

    if len(username) < 4:
        return {
            "valid": False,
            "message": "Username must be at least 4 characters"
        }

    # Password validation
    if not isinstance(password, str):
        return {
            "valid": False,
            "message": "Password must be a string"
        }

    if len(password) < 8:
        return {
            "valid": False,
            "message": "Password too short"
        }

    # Check for at least one digit
    has_digit = False

    for char in password:
        if char.isdigit():
            has_digit = True
            break

    if not has_digit:
        return {
            "valid": False,
            "message": "Password must contain at least one digit"
        }

    return {
        "valid": True,
        "message": "Login Accepted"
    }


checks = [
    ("ajit", "ajit1234"),
    ("raj", "raj12345"),
    ("mohan", "password"),
    ("", "abc12345")
]

for username, password in checks:
    print(check_login(username, password))