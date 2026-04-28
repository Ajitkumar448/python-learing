NAME ="AJIT" 
DATE = "12/04/2026"
LETTER = '''Dear {NAME}
you are selected!
{DATE}'''
print(LETTER.format(NAME=NAME,DATE=DATE))
double_space_string = "this  is a double space string"
if "  " in double_space_string:
    print("double space detected")
else:
    print("no double space")
single_space_string = double_space_string.replace("  " , " ")
print(single_space_string)
letter = "Dear harry,\nthis course is awesome.\nthanks!"
print(letter)

