print("Enter size of list")
n = int(input())
l = []
num = 0
print("Enter the elements")
for i in range(0, n, 1):
    num = int(input())
    l.append(num)
print(l)
sum = 0
for i in l:
    sum = sum + pow(i,3)
print(sum)
