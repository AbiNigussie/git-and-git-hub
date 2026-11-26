file_name = input("Enter file name: ")
count = 0
with open(file_name, "r") as file:
    for line in file:
        count += 1
print("total lines:",  count)