import re
employees = [
    {
        "name": "Ajit",
        "employee_id": "E101",
        "age": 24,
        "department": "IT",
        "salary": 45000
    },

    {
        "name": "Priya",
        "employee_id": "E102",
        "age": 17,
        "department": "HR",
        "salary": 50000
    }
]
def find_invalid_employees(name, employee_id, age, department, salary):
    constraints = {"name": isinstance(name,str)and len(name) > 0,
                   "employee_id": isinstance(employee_id,str) and
                   re.fullmatch ("E\d+",employee_id,re.IGNORECASE),
                   "age" : isinstance(age,int) and age>=18,
                   "department": isinstance(department,str) and department in("IT", "HR", "Finance", "Marketing"),
                   "salary" : isinstance(salary,int) and salary > 0}
    return[key for key,value in constraints.items()if not value]

def validate_data(data):
    is_sequence = isinstance(data,(list , tuple))
    if not is_sequence:
        print("invalid format: expected list bor tuple")
        return False
    is_invalid= False
    key_set= set(["name",
                  "employee_id",
                  "age",
                  "department",
                  "salary"])
    for index,dictionary in enumerate(data):
        if not isinstance(dictionary,dict):
            print(f"invalid farmat:expected a dictionary at position {index}")
            is_invalid =True
            continue
        if set(dictionary.keys()) != key_set:
            print(f"In {dictionary} a missing or invalid key at position{index}")
            is_invalid = True
            continue
        invalid_records =find_invalid_employees(**dictionary)
        for key in invalid_records:
         print(f"unexpected format '{key} :{dictionary[key]}' at postion {index}")
        is_invalid = True
    if is_invalid:
        return False
    print("valid format.")
    return True
validate_data(employees)