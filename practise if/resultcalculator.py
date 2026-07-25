def result(name,marks,percentage):
    if marks<0:
        return "Invalid marks"
    elif marks>500:
        return"marks should be in between 0 to 500"
    elif marks>=450:
        return f"{name} got A+ grade with {percentage:.2f}%"
    elif marks>=400:
        return f"{name} got A grade with {percentage:.2f}%"
    elif marks>=350:
        return f"{name} got B grade with {percentage:.2f}%"
    elif marks>=300:
        return f"{name} got C grade with {percentage:.2f}%"
    elif marks >=250:
        return f"{name} got D grade with {percentage:.2f}%"
    elif marks>=200:
        return f"{name} got E grade with {percentage:.2f}%"
    else:
        return f"{name} is fail"

name = input("enter name: ")
marks = int(input("enter marks: "))
percentage = (marks/500)*100

print(result(name, marks, percentage))
def process_student(name, marks):

    # Name validation
    if not isinstance(name, str) or len(name.strip()) == 0:
        return {
            "valid": False,
            "message": "Invalid name"
        }

    # Marks validation
    if not isinstance(marks, int):
        return {
            "valid": False,
            "message": "Marks must be an integer"
        }

    if marks < 0 or marks > 100:
        return {
            "valid": False,
            "message": "Marks must be between 0 and 100"
        }

    # Grade calculation
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "Fail"

    # Status calculation
    if marks >= 40:
        status = "Pass"
    else:
        status = "Fail"

    return {
        "name": name,
        "marks": marks,
        "grade": grade,
        "status": status
    }


students = [
    ("Ajit", 82),
    ("Ravi", 105),
    ("", 75),
    ("Neha", 35)
]

for name, marks in students:
    print(process_student(name, marks))