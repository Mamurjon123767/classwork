def number_checker(num):
    if not isinstance(num, int):
        print("only integer data type is allowed")
    if num > 0:
        print("number is positive")
    elif num < 0:
        print("number is negitive")
    else:
        print("zero")