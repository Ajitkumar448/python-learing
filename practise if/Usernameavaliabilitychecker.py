def check_username_availiablity(username):
 taken_usernames = ["john_doe", "jane_smith", "user123"]
 if username == "":
        return"username cannot be empty"
 elif " " in username:
        return"there is no space in between username"
 elif len(username)<4 or len(username)>10:
        return"username must in between 4 to 10 characters"
 elif username.lower() in taken_usernames:
        return"already taken"
 
 else:
        return"username is available"

username = input("enter name: ")

print(check_username_availiablity(username))
    
    