students = [
 {
    "name": "ajit",
    "id": 1,
    "age": 20,
    "subject" :"MCA",
    "Marks": 80
    
  },
 {
    "name": "amit",
    "id": 2,
    "age": 22,
    "subject": "MBA",
    "Marks": 85
 },
 {
    "name": "ajay",
    "id": 3,
    "age": 21,
    "subject": "MSc",
    "Marks": 88
 }
]

def find_invalid_students(name, id, age, subject, Marks):
    constraints= {
        "name" : isinstance (name,str)and len(name) > 0,
        "id" : isinstance(id,int),
        "age" : isinstance(age,int),
        "subject" : isinstance(subject,str),
        "Marks" : isinstance(Marks,int)
    }
    return [key for key, value in constraints .items() if not value ]

def validate_data(data):
    is_sequence = isinstance(data,(list,tuple))
    if not  is_sequence:
        print("invalid format:expected a list or tuple")
        return False
    is_invalid = False
    key_set = set([
        "name",
        "id",
        "age",
        "subject",
        "Marks"
    ])
    for index,dictionary in enumerate(data):
        if not isinstance(dictionary,dict):
            print(f"invalid format:expected a dictionary at position {index}")
            is_invalid= True
            continue
        if set(dictionary.keys()) != key_set:
            print(f"invalid format:{dictionary} at position {index} has a missing or invalid key")
            is_invalid = True
            continue
        invalid_record = find_invalid_students(**dictionary)

        for key in invalid_record:
          print( f"Unexpected format '{key}: {dictionary[key]}' at position {index}.")
          is_invalid = True
    if is_invalid:
        return False
    print("valid format.")
    return True
validate_data(students)

    



 


  