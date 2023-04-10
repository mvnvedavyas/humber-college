"""The objective of this application is to demonstrate the use of file-based systems, dictionaries, conditional and
control statements, functions with passed values and return values, search and display data, and formatted report
display. This application aims to cover various programming concepts while managing an inventory system.

a) Enter choice 2 to display inventory, without adding items in the inventory
b) Enter choice 3 to search and display inventory items, without adding any item in the inventory
c) Choose option other than the valid choices (1, 2, 3, or 5). It could be alphabet or numeric value
d) Add two to three items in inventory and display using option 2.
e) Add an item having identical Serial Code to an existing item in the inventory to show that quantity is updated without updating the item price
f) Add an item having identical Serial Code to existing item in inventory, but having higher item unit price to show the update in inventory quantity as well as inventory price (unit price)
g) Search inventory when Item is in the inventory
h) Search inventory when Item is NOT in the inventory.
i) Enter valid choice as option as well as invalid choice as an option (to show the messages displayed
j) Demonstrate how application ends.

Author: Venkata Narasimha Vedavyas Muppavarapu
Date: 7th feb, 2023
studentId : N01583267

"""
import json
import datetime
# import date
import mypassword

# Configure the filename value as we that is in project to access
config = {
    "inv": "inventory.txt",
    "sales": "salesinvoice.txt",
    "mailfrom" : "vdvs99@gmail.com",
    "mailto" : "vdvs99@gmail.com"
}


def display_info():
    """
    Function to display banner of student name and student ID when students list is asked for display
    Updated : 8th feb 23

    :return:
    """
    studentId = "N01583267"
    name = "Venkata Narasimha Vedavyas Muppavarapu"
    print("%120s\n" % name)
    print("%120s\n" % studentId)


def read_file(filename=config["inv"]):
    """
    Read the file and return a dictionary of items
    Updated : 8th feb 23

    :param filename:
    :return inv_dict:
    """
    try:
        with open(filename, "r") as file:
            file = file.readlines()
            inv_dict = json.loads(file[0])
            return inv_dict
    except OSError as e:
        print(f"{e}")


def write_file(inventory, filename=config["inv"]):
    """
    Write the data to the file
    Updated : 8th feb 23

    :param inventory:
    :param filename:
    :return boolean:
    """
    try:
        with open(filename, "w+") as file:
            clean = json.dumps(inventory)  # adding inventory to file
            file.write(clean)
            return True
    except OSError as e:
        print(f"{e}")
        return False


def gen_invoice(selected_item, serial_code, quantity):
    """
    Generate invoice in sepearate function setting values to key's and return
    :param selected_item:
    :param serial_code:
    :param quantity:
    :return:
    """
    return {
        "time": datetime.datetime.now().isoformat(),
        "name": selected_item["name"],
        "serial": serial,
        "quantity": quantity,
        "price": selected_item["price"],
    }


def calc_total_tax_subtotal(list_of_items):
    """
    Calculate total tax subtotal
    Updated : 19th feb 23
    :param list_of_items:
    :return:
    """
    total = 0
    for item in list_of_items:
        total = total + (item["quantity"] * item["price"])
    return {
        "total": total,
        "tax": round(total * 0.13, 2),
        "grand_total": round(total * 1.13, 2),
    }


def add_items():
    """
    Function for taking inputs of name, serial, quantity, price from user
    Updated : 8th feb 23

    :param :
    :return dictionary with inventory entered:
    """
    inventory = read_file()  # reading file, in order to keep file ready when valid inputs are entered
    name = input("Enter item name: ")
    serial = input("Enter item serial number: ")
    quantity = int(input("Enter quantity of Items: "))
    price = float(input("Enter price per unit: \t$"))
    print("Searching if item with seria code " + serial
          + "already exists in items history")
    if not inventory:  # checking if inventory is empty
        print("Item" + name + " inventory with serial code" + serial + " does not have any items. Adding new items! ")
    elif serial in inventory:  # if inventory is not empty, proceeding to update quantities and price depends on the
        # scenario
        print("Item exists in inventory. Updating the item Information")
        inventory[serial]['quantity'] += quantity  # update the quantity
        print("Item Quantity has been updated.")
        if price > inventory[serial]['price']:  # checking user's price if it is greater than dictionary price
            inventory[serial]['price'] = price
            print("Item Price is updated! Thankyou.")
        write_file(inventory)
        return
    else:
        print("Item is not in inventory.Adding item" + name + " to inventory ")

    inventory[serial] = {'name': name, 'quantity': quantity, 'price': price}  # adding inventory to the dictionary
    write_file(inventory)
    print("Item with " + serial + "added to inventory.")


def ca_spaces(_str, length=22, price=False):
    # ca = calculate & append _spaces
    __str = str(_str)

    if len(str(_str)) >= length:
        return _str
    if price:
        return str("&nbsp;" * (length - len(__str) - 1)) + "$" + __str
    return str("&nbsp;" * (length - len(__str))) + __str


def send_mail(data):
    # Send inventory report to the user
    email_invoice_list = ""
    for item in data["list"]:
        email_invoice_list += f"""  , 36){ca_spaces(item["name"])}{ca_spaces(item["serial_code"], 8)}{ca_spaces(item["quantity"])}{ca_spaces(item["ppu"], price=True)}\n    """
    email_text = f"""<pre>\n
    {"-" * 110}
    {ca_spaces("Suraj Mandal", 110)}
    {ca_spaces("N01537188", 110)}
    {("-" * 110)}
    {(ca_spaces("Sale Time", 36) + ca_spaces("Name") + ca_spaces("ID", 8) + ca_spaces("Quantity") + ca_spaces("Price Per Unit"))}
    {email_invoice_list}
    {("-" * 110)}
    {ca_spaces("Total price of all items purchased:", 70) + ca_spaces(round(data["total"]["total"], 2), length=30, price=True)}
    {ca_spaces("Tax amount paid:", 70) + ca_spaces(round(data["total"]["tax"], 2), length=30, price=True)}
    {ca_spaces("Total amount paid:", 70) + ca_spaces(round(data["total"]["grand_total"], 2), length=30, price=True)}
    {("-" * 110)}
    </pre>
    \n
    """

    email = {
        "subject": f"My Sales Invoice to {datetime.today().strftime('%B %d, %Y')}",
        "data": email_text,
        "password": mypassword.mypassword,
        "from": config["mailfrom"],
        "to": config["mailto"],
    }

    import ssl
    import smtplib
    from email.message import EmailMessage

    msg = EmailMessage()
    msg["Subject"] = email["subject"]
    msg["From"] = email["from"]
    msg["To"] = email["to"]
    msg.set_content(email["data"], subtype="html")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email["from"], email["password"])
        smtp.send_message(msg)

    return True


def sales_invoice():
    # Sales invoice function, to be implimented in the next lab
    serial_code = input("\tEnter inventory item serial code: ")
    quantity = int(input("\tEnter inventory item quantity: "))

    inventory = read_file()
    invoice = read_file(file_name=config["sales"])

    selected_item = None
    write_invoice = invoice
    write_inventory = inventory

    for item in list(inventory):
        if item == serial_code:
            selected_item = inventory[item]
            gi = gen_invoice(
                selected_item, serial_code, quantity
            )  # This makes the code more readable below
            # Check if the quantity is available
            if selected_item["quantity"] < quantity:
                print("Not enough quantity available..")
                return False
            elif selected_item["quantity"] == quantity:
                write_inventory.pop(item)
                write_invoice["list"].append(gi)
                write_invoice["total"] = calc_total_tax_subtotal(write_invoice["list"])
            else:
                write_inventory[item]["quantity"] -= quantity
                write_invoice["list"].append(gi)
                write_invoice["total"] = calc_total_tax_subtotal(write_invoice["list"])

    if selected_item is None:
        print("Item is not in inventory..")
        return False

    # Send mail to the customer
    print("Sending mail to the customer...")
    if send_mail(write_invoice) is False:
        print("Error sending mail, transaction has been reverted...\n")
        return False
    # Write to the file
    write_file(write_invoice, config["sales"])
    write_file(write_inventory, config["inv"])


def display_inventory():
    """
    Function to display all items in the inventory
    Updated : 8th feb 23

    :return:
    """
    inventory = read_file()
    if inventory:
        display_info()  # displays student name and id
        print("%30s%30s%30s%30s\n" % ("Item Name", "Item Serial Code", "Item Quantity", "Item Price per Unit"))
        for serial, item in inventory.items():
            # printing for every record.
            print("%30s%30s%30s%30s\n" % (item['name'], serial, item['quantity'], "$" + str(round(item['price'], 2))))
    else:
        print("Inventory is empty.There are no inventory items to display! Please enter Inventory \n")


def search_item():
    """
    Function to search for a specific item by serial number
    Updated : 8th feb 23

    :return:
    """
    inventory = read_file()  # read file to save it to inventory dictionary
    if not inventory:
        print("Inventory is empty.There are no inventory items to display! Please enter Inventory \n")
    else:
        serial = input("Enter item serial number to search: ")
        # checking if serial exists in inventory
        if serial in inventory:
            print("Item is available in inventory with serial code - " + serial)
            item = inventory[serial]
            display_info()
            print("%30s%30s%30s%30s\n" % ("Item Name", "Item Serial Code", "Item Quantity", "Item Price per Unit"))
            print("%30s%30s%30s%30s\n" % (item['name'], serial, item['quantity'], "$" + str(round(item['price'], 2))))

        elif serial not in inventory:
            print("Item with serial number " + serial + " is not currently in inventory.")


def main():
    """
    Main function with menu for user to select an option
    Updated : 8th feb 23

    :return:
    """
    # Define the inventory as a dictionary
    inventory = {}
    while True:
        # Printing to get input from the options
        print("Inventory Management System")
        print("\t 1. Add Inventory Items")
        print("\t 2. Display All Inventory Items")
        print("\t 3. Search Inventory Item By Item Serial Code")
        print("\t 4. Sales")
        print("\t 5. Exit/End Application")

        # Taking input from the user choice
        choice = input("Please enter your choice: ")

        # Handle invalid input
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please enter a valid choice.")
            continue

        # Add item
        if choice == "1":
            add_items()
        # Display inventory
        elif choice == "2":
            display_inventory()
        # Search item
        elif choice == "3":
            search_item()
        # Sales
        elif choice == "4":
            sales_invoice()
        # Exit the application
        elif choice == "5":
            print("Application ending now!!")
            break


if __name__ == '__main__':
    main()
