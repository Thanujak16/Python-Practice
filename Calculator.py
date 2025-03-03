print("Enter 1st No.")

a = int(input())
print("Enter 2nd No.")
b = int(input())
print("Enter your operator")
operator = input()

if operator == "+":
    sum = a+b
    print(sum)
elif operator == "-":
    minus = a-b
    print(minus)
elif operator == "*":
    multiply = a*b
    print(multiply)
elif operator == "/":
    if b == 0:
        print("Not Defined")
    else:
        divide = a/b
        print(divide)
elif operator == "%":
    if b ==0:
        print("Not Defined")
    else:
        rem = a%b
        print(rem)
else:
    print("Wrong operator")
