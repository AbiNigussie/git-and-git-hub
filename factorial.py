n = int (input("Enter integer number: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i

"""print ("factorial of ", n, "is ", factorial)
#reverse a number
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i, end="") """
n = int (input ("Enter the number: "))
for i in range(1, 11):
    result = n*i
print(n, "x", i, "=", result)
n = int(input("Enter a number: "))

for i in range(1, 11):
    result = n * i
    print(n, "x", i, "=", result)
n = int(input("Enter a number: "))
count = 0
while n>0:
    n= n//10
    count +=1
print("The number has ", count, "digits")