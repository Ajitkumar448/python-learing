import re
users = [
    {
        "username": "ajit123",
        "password": "pass@123",
        "age": 21
    },
    {
        "username": "",
        "password": "123",
        "age": 15
    },
    {
        "username": "rohit@",
        "password": "admin123",
        "age": 19
    }
]


def find_invalid_users(username, password, age):
    constraints = {"username": isinstance(username,str) and len(username) > 0 and re.fullmatch(r"[a-zA-Z0-9]+", username),
                   "password": isinstance(password,str) and len(password) >= 6,
                   "age":isinstance(age,int) and age>=18
                   }
    return[key for key,value in constraints.items()if not value]
def validate_data(data):
    is_sequence = isinstance(data,(list,tuple))
    if not is_sequence:
        print("invalid format: expected a list or tuple")
        return False
    is_invalid = False
    key_set = {"username",
               "password",
               "age"}
    for index, dictionary in enumerate(data):
        if not isinstance(dictionary,dict):
            print(f" invalid format: expected a dictionary at position {index}")
    
            is_invalid = True
            continue
        if set(dictionary.keys())!= key_set:
            print(f"in {dictionary} a missing or invalid key at position {index}")
            is_invalid = True
            continue
        invalid_record = find_invalid_users(**dictionary)
        for key in invalid_record:
         print(f"unexpected format'{key}: {dictionary[key]}' at position {index}")
         is_invalid = True

    if is_invalid:
        return False
    print("valid format.")
    return True
validate_data(users)



