def number_pattern(n):

    if not isinstance(n, int):
        return "Argument must be an integer value."

    if n < 1:
        return "Argument must be an integer greater than 0."

    result = ""

    for i in range(1, n + 1):
        result += str(i) + " "
        print(result)
    return result.strip()

# print(number_pattern(5))
def number_pattern(n):

    if not isinstance(n, int):
        print("Argument must be an integer value.")
        return

    if n < 1:
        print("Argument must be an integer greater than 0.")
        return

    result = ""

    for i in range(1, n + 1):
        result += str(i) + " "

    print(result)

number_pattern(4)
def number_pattern(n):

    if not isinstance(n, int):
        print("Argument must be an integer value.")
        return

    if n < 1:
        print("Argument must be an integer greater than 0.")
        return

    for i in range(1, n + 1):
        print(i, end=" ")

number_pattern(4)
