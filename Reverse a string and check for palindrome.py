print("Enter a string")
a = input()

rav_a = a[::-1]

print(rav_a)

if a == rav_a:
    print("palindrome")
else:
    print("Not a palindrome")
