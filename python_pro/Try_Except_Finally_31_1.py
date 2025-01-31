class Handle:
    def abc(self):
        try:
            a = 10
            b = 5
            result = a / b
            print(f"The result of {a} divided by {b} is: {result}")
        except Exception:
            print("Error occurred")
        else: #both runs when no exception here
            result = a + b
            print(f"The result of {a} addition {b} is: {result}")
        finally:
            print("Code is Working Properly")
handle_instance = Handle()
handle_instance.abc()

#custom & raising exception
# Custom Exception class
class NegativeValueError(Exception):
    pass

# Function to check if number is positive
def check_positive_number(number):
    if number < 0:
        raise NegativeValueError("Error: Negative numbers are not allowed.")  #raising exception (here the exceptions are predefines by python)
    return number

#Custom exception
try:
    number = int(input("Enter a number: "))
    check_positive_number(number)
    print(f"You entered: {number}")
except NegativeValueError as e:
    print(e)