# IMPORTS
# This function is so we can display data as a table more easily
from tabulate import tabulate

# CLASSES
# This class will be used to create a shoe object representing a shoe in store inventory
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # These getters are used to get properties of the object while adhering to the OOP principle of encapsulation for data protection
    def get_country(self):
        return self.country    
    def get_code(self):
        return self.code
    def get_product(self):
        return self.product
    def get_cost(self):
        return self.cost
    def get_quantity(self):
        return self.quantity

    # This is used to represent the object as a string in below format
    def __str__(self):
        return f"""Country:    {self.country}        
Code:       {self.code}
Product:    {self.product}
Cost:       {self.cost}
Quantity:   {self.quantity}"""


# FUNCTIONS
def read_shoes_data():
    """Update shoe_list variable with inventory.txt file"""
    try:
        with open("inventory.txt", "r") as inventory_file:
            for index, line in enumerate(inventory_file):
                if index != 0:
                    country = line.strip().split(",")[0]
                    code = line.strip().split(",")[1]
                    product = line.strip().split(",")[2]
                    cost = int(line.strip().split(",")[3])
                    quantity = int(line.strip().split(",")[4])
                    shoe_list.append(Shoe(country, code, product, cost, quantity))
    except FileNotFoundError:
        print("Inventory file does not exist. Please contact Support.")

def add_shoe_list_to_inventory_file():
    """Update inventory.txt with updated shoe_list"""
    new_shoe_list = []

    for shoe in shoe_list:
        new_shoe_list.append(f"\n{shoe.get_country()},{shoe.get_code()},{shoe.get_product()},{shoe.get_cost()},{shoe.get_quantity()}")

    with open("inventory.txt", "w") as inventory_file:
        inventory_file.write(f"Country,Code,Product,Cost,Quantity{''.join(new_shoe_list)}")


def capture_shoes():
    """Add information about a new shoe to shoe_list"""

    country = input("Please enter the country of the shoe: ").strip()
    code = input("Please enter the code of the shoe: ").strip()
    product = input("Please enter the name of the shoe: ").strip()

    # User is asked input a whole positive number, and is asked to retry if they do not
    while True:
        try:
            cost = int(input("Please enter the cost of the shoe to the nearest whole number (e.g. 23): "))
        except ValueError or cost < 0:
            print("Please enter a whole number in the format as shown in the example...")
            continue
        if cost < 0:
            print("Please enter a positive whole number in the format as shown in the example...")
            continue
        break 

    # User is asked input a whole positive number, and is asked to retry if they do not           
    while True:
        try:
            quantity = int(input("Please enter the quantity of stock of the shoe (e.g. 55): "))
        except ValueError:
            print("Please enter a whole number in the format as shown in the example...")
            continue
        if quantity < 0:
            print("Please enter a positive whole number in the format as shown in the example...")
            continue
        break

    # Shoe is added to shoe_list here
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    print("You have succesfully added an item to inventory!")

def view_all():
    """Display all shoes as a table"""
    table = [["Country", "Code", "Product", "Cost", "Quantity"]]
    for shoe in shoe_list:
        table.append([
            shoe.get_country(), shoe.get_code(), shoe.get_product(), shoe.get_cost(), shoe.get_quantity()
        ])
    print(tabulate(table, headers="firstrow"))

def value_per_item():
    """Display all shoes as a table, including value of each shoe"""
    table = [["Country", "Code", "Product", "Cost", "Quantity", "Value (Cost x Quantity)"]]
    for shoe in shoe_list:
        table.append([
            shoe.get_country(), shoe.get_code(), shoe.get_product(), shoe.get_cost(), shoe.get_quantity(), shoe.get_cost() * shoe.get_quantity()
        ])
    print(tabulate(table, headers="firstrow"))

def re_stock():
    """Display shoe with lowest quantity, and add stock to it after user confirms they wish to add and enters how much the want to add"""
    # If no shoes in stock, a message is displayed stating that
    if len(shoe_list) < 1:
        return print("No shoes are in stock...")

    # The shoes with lowest stock is found here (if two or more tie for lowest quantity, then the first is displayed)
    index_of_shoe_with_lowest_quantity = 0
    for index, shoe in enumerate(shoe_list):
        if shoe.get_quantity() < shoe_list[index_of_shoe_with_lowest_quantity].get_quantity():
            index_of_shoe_with_lowest_quantity = index
    print(f"""Shoe with the lowest quantity:
{shoe_list[index_of_shoe_with_lowest_quantity]}""")

    # User is asked to confirm if they want to re-stock
    is_restocking = input("Please enter 'Yes' to restock or 'No' to not restock: ").strip().lower()

    # If user enters 'Yes', then they are asked for a positive whole number (if they choose 0, 
    # they have changed their mind since entering 'Yes', and they can do that)
    match is_restocking:
        case "yes":
            while True:
                try:
                    restock_quantity = int(input("Please enter the quantity of shoe you would like to restock (e.g. 55): "))
                except ValueError:
                    print("Please enter a whole number in the format as shown in the example...")
                    continue
                if restock_quantity < 0:
                    print("Please enter a positive whole number in the format as shown in the example...")
                    continue
                break
            
            # This updates the shoe_list to reflect addition of stock to shoe
            shoe_list[index_of_shoe_with_lowest_quantity].quantity = shoe_list[index_of_shoe_with_lowest_quantity].quantity + restock_quantity
            # This updates the inventory.txt file with the updated shoe_list
            add_shoe_list_to_inventory_file()
            print("The shoe has been successfully restocked!")
        # This message whether user enters 'No' or an invalid entry    
        case _:
            print("The shoe has not been restocked")

def seach_shoe():
    """Ask user to enter case-sensitive shoe code, and display the shoe if found"""
    search_code = input("Please enter the code of shoe you want to search for (case-sensitive): ").strip()

    for shoe in shoe_list:
        if shoe.get_code() == search_code:
            return print(shoe)
    return print("The shoe has not been found...")

def highest_qty():
    """Display shoe with highest quantity and inform user the shoe is to be put on sale"""
    # If no shoes in stock, a message is displayed stating that
    if len(shoe_list) < 1:
        return print("No shoes are in stock...")

    # This finds the shoe with highest quantity
    index_of_shoe_with_highest_quantity = 0
    for index, shoe in enumerate(shoe_list):
        if shoe.get_quantity() > shoe_list[index_of_shoe_with_highest_quantity].get_quantity():
            index_of_shoe_with_highest_quantity = index

    print(f"""Shoe to be put on sale:
{shoe_list[index_of_shoe_with_highest_quantity]}""")


# VARIABLES
shoe_list = []

# MAIN
# This updates shoe_list with inventory.txt
read_shoes_data()

while True:
    user_choice = input(
f"""Please enter an option from the menu below:
ats - Capture data about a shoe and add it to inventory
va - view inventory of all shoes
vv - view value of inventory of all shoes
sfs - search for a shoe and display its data
rs - restock shoe with lowest inventory
hq - view the current item to be put for sale (the one with the highest quantity)
: """
).strip().lower()
    
    match user_choice:
        
        case "ats":
            # This adds shoe to shoe_list
            capture_shoes()
            # This updates inventory.txt with updated shoe_list
            add_shoe_list_to_inventory_file()
        case "va":
            view_all()
        case "vv":
            value_per_item()
        case "sfs":
            seach_shoe()
        case "rs":
            re_stock()
        case "hq":
            highest_qty()
        case _:
            print("This entry is invalid...Please try again...")
