def greet():
    print("hello, Likhibra Academy")
greet()
def greet(name):
    print(f"hello, {name} welcame to lkhibra academy!")
greet("abi")
def squear(n):
    return n*n
print (squear(5))
def greet(name = "student"):
    print(f"hello, {name}")
greet()
greet("alemu")
academy = "lkhibra"
def dis_academy():
    print("the best academy is ", academy)
dis_academy()
def mes():
    mesa = "vbdvhbn sdc!"
    print("Inside function: ", mesa)
mes()
n = int(input("enter a number: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n* factorial(n-1)
num =n
result = factorial(num)
print("factorial of ", num, "is", result)