print("Enter a Number")
a = int(input())
rem = 0
sum = 0
while a>0:
    rem = a%10
    sum = sum + rem
    a = a//10
print(sum)
