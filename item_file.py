items =input("Enter grocery items: ")
with open("transaction.txt", "w") as file:
    file.write(items + "\n")
with open("transaction.txt", "r") as file:
    items = file.read()
print("\n  Your Grocery List:")
for item in items:
    print(items)