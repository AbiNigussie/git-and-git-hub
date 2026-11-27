
import json
import os

FILE_NAME = "inventory.json"


# Load inventory from file
def load_inventory():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


# Save inventory to file
def save_inventory():
    with open(FILE_NAME, "w") as file:
        json.dump(inventory, file, indent=4)


# Add a new product
def add_product():
    product_id = input("Enter product ID: ")

    if product_id in inventory:
        print("Product ID already exists!")
        return

    name = input("Enter product name: ")

    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        if quantity < 0 or price < 0:
            print("Quantity and price cannot be negative!")
            return

        inventory[product_id] = {
            "name": name,
            "quantity": quantity,
            "price": price
        }

        save_inventory()
        print("Product added successfully!")

    except ValueError:
        print("Please enter valid numbers!")


# Display all products
def view_products():
    if not inventory:
        print("No products available.")
        return

    print("\n========== PRODUCT LIST ==========")

    print(f"{'ID':<10}{'Name':<20}{'Quantity':<12}{'Price':<10}")

    for product_id, product in inventory.items():
        print(
            f"{product_id:<10}"
            f"{product['name']:<20}"
            f"{product['quantity']:<12}"
        )


# Search for a product
def search_product():
    product_id = input("Enter product ID to search: ")

    if product_id in inventory:
        product = inventory[product_id]

        print("\nProduct Found!")
        print("ID:", product_id)
        print("Name:", product["name"])
        print("Quantity:", product["quantity"])
        print("Price:", product["price"], "ETB")
    else:
        print("Product not found!")


# Update product information
def update_product():
    product_id = input("Enter product ID to update: ")

    if product_id not in inventory:
        print("Product not found!")
        return

    product = inventory[product_id]

    try:
        print("1. Update Name")
        print("2. Update Quantity")
        print("3. Update Price")

        choice = input("Choose option: ")

        if choice == "1":
            product["name"] = input("Enter new name: ")

        elif choice == "2":
            quantity = int(input("Enter new quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative!")
                return
            product["quantity"] = quantity

        elif choice == "3":
            price = float(input("Enter new price: "))
            if price < 0:
                print("Price cannot be negative!")
                return
            product["price"] = price

        else:
            print("Invalid choice!")
            return

        save_inventory()
        print("Product updated successfully!")

    except ValueError:
        print("Invalid input!")


# Sell products
def sell_product():
    product_id = input("Enter product ID: ")

    if product_id not in inventory:
        print("Product not found!")
        return

    try:
        quantity = int(input("Enter quantity to sell: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

        product = inventory[product_id]

        if quantity > product["quantity"]:
            print("Insufficient stock!")
            return

        product["quantity"] -= quantity

        total = quantity * product["price"]

        save_inventory()

        print("\nSale completed successfully!")
        print("Product:", product["name"])
        print("Quantity sold:", quantity)
        print("Total amount:", total, "ETB")
        print("Remaining stock:", product["quantity"])

    except ValueError:
        print("Please enter a valid quantity!")


# Delete a product
def delete_product():
    product_id = input("Enter product ID to delete: ")

    if product_id in inventory:
        del inventory[product_id]
        save_inventory()
        print("Product deleted successfully!")
    else:
        print("Product not found!")


# Generate inventory report
def inventory_report():
    total_products = len(inventory)
    total_items = sum(p["quantity"] for p in inventory.values())
    total_value = sum(
        p["quantity"] * p["price"]
        for p in inventory.values()
    )

    print("\n========== INVENTORY REPORT ==========")
    print("Total Product Types:", total_products)
    print("Total Items in Stock:", total_items)
    print("Total Inventory Value:", total_value, "ETB")


# Main program
inventory = load_inventory()

while True:
    print("\n===================================")
    print("       INVENTORY MANAGEMENT")
    print("===================================")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Sell Product")
    print("6. Delete Product")
    print("7. Inventory Report")
    print("8. Exit")
    print("===================================")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_product()

    elif choice == "5":
        sell_product()

    elif choice == "6":
        delete_product()

    elif choice == "7":
        inventory_report()

    elif choice == "8":
        print("Thank you for using Inventory Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
