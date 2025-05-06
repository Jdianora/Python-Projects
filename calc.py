def addition(x,y):
    return x+y
def subtraction (x,y):
    return x-y
def multiplication (x,y):
    return x*y
def division (x,y):
    return x/y

results = []

print ("Please Select Which Operation You'd Like To Use.")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")

while True:
    user_select = input("Use values 1 - 4 To Select Your Operation:")
    if user_select in ('1', '2', '3', '4'):
        try:
            val1 = float(input("Insert First Value:"))
            val2 = float(input("Insert Second Value:"))
        except ValueError:
            print("Invalid Input. Please Enter Number.")
            continue
    if user_select == '1':
        print(val1, "+", val2, "=", addition(val1, val2))
    elif user_select == '2':
        print(val1, "-", val2, "=", subtraction(val1, val2))
    elif user_select == '3':
        print(val1, "*", val2, "=", multiplication(val1, val2))
    elif user_select == '4':
        print(val1, "/", val2, "=", division(val1, val2))

    continue_math = input("Did You Want To Continue? (yes/no)")
    if continue_math == "no":
        break
    else:
        print("Invalid Input")