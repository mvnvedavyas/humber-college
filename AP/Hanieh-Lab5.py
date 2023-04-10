"""
Application Name:           Hanieh-lab3.py
Author/Developer:           Hanieh Moghaddasi
Date:                       January 26th, 2023

This application is to keep reocrd of items and their informations. You can add items and they are 
some conditions if the item exists or not exists. You can search the item based on serial code. you 
can display all the items. All the data is saving in the text file. When custoemr buy something, the 
email will be send, and the data will be updated too.

This application has functions to:
separate_enteries(): It's just sepearte the line by -*-

my_filename(): get the file from the path
display_info(): Display options to choose 1. Add item in inventory 2. Display inventory items
 3. Search inventory item by serial code 4. End application

display_my_info() : to display your name and student ID.

add_items(my_dict): Everything is saving in the text file, and the data is appending each time to the text file,
and teh data is reading from the text file. Inserting items into the dictionary. Serial code is unique.
Serial code can't be repeated, but the other information can. If user enters an identical item Serial Code,
that is already part of the items inventory (name may or may not be the same), system updates the quantity
by taking previous saved quantity in the dictionary and adding a new quantity to the previous value. Also,
the new price entered is less than the previously saved item price per unit, then the lower price is not 
updated in the inventory records

display(my_dict):display all items with all of their values

send_email(): when a customer buy someting from the inventory, it will send an email 
display_date(): it shows the date and time of sell
display_sale_info(): It display what customer is buying in a row
sale(): it shows the calulation for the sale. It calculate the tax and total amount to pay.
search_based_on_serial_code(my_dict,serial_no):  search and display an item from the item record (dictionary). If item does
 not exist, give an error message.
enter_item_info: It aske user to enter input for item name, serial code, quantity, and price.
main(): call all function and run the application and show the messages.
"""
import os
import ast
from pathlib import Path
from datetime import datetime
from email.message import EmailMessage
import smtplib
import json



def my_filename():
    writepath = '/Users/haniehmoghaddasi/Desktop/Humber/Application Programming - CCGC-5003-0NA/Labs/Lab5/'
    mytextFile = 'mytext'
    filename_txt = mytextFile+'.txt'
    filename = writepath+filename_txt
    return filename
    
def separate_enteries():
    my_line = ("-*-"*40) + "\n"
    print(my_line)

def display_info():
    options = f"1. Add inventory items{os.linesep}2. Display all inventory items{os.linesep}3. Search an item{os.linesep}4. Sales Invoice{os.linesep}5.End Appilcation"
    print(options)
    choice=input("\n"+"Please enter your choice:\t\t")
    return choice

def display_my_info():
    my_info = {"fullname":"Hanieh Moghaddasi","student_no":"N00727363"}
    fullname = "%121s"%my_info['fullname']
    student_no = "%120s"%my_info['student_no']
    return fullname, student_no

def add_items(my_dict):
    item_name,item_serial_code,qty_per_item,price_per_unit = enter_item_info()
    filename = my_filename() 
    my_dic_length = len(my_dict)
    if any(item_serial_code in x.values() for x in my_dict.values()) :
        print(f"Checking inventory, if this item with item code {item_serial_code} already exists .......")
        print("This item is alreday exists in inventory …. Updating item information ….")
        
        for k,v in my_dict.items():
            # updated_qty =  qty_per_item+v["Qty per item"]
            if price_per_unit > v["Price per unit"]:
                v["Price per unit"] = price_per_unit
                v["Qty per item"] += qty_per_item
            else:
                v["Qty per item"] = v["Qty per item"]+qty_per_item
        separate_enteries()
        if os.path.exists(filename):
            with open( filename, 'w') as f:
                f.write(str(my_dict)+"\n")

    elif not any(item_serial_code in x.values() for x in my_dict.values()):
        if len(my_dict) == 0:
            count = 1
            case = {
                "Item name":item_name,
                "Serial code":item_serial_code,
                "Qty per item":qty_per_item,
                "Price per unit":price_per_unit
                }
            print("Ineventory does not have any items...\nAdding new item in inventiry ... \nFirst item information saved ....")
            separate_enteries()
            my_entry = {count:case}
            my_dict.update(my_entry) 
            if os.path.exists(filename):
                with open( filename, 'w') as f:
                    f.write(str(my_dict)+"\n")

        else:
            case = {
            "Item name":item_name,
            "Serial code":item_serial_code,
            "Qty per item":qty_per_item,
            "Price per unit":price_per_unit
            }
            my_entry = {my_dic_length+1:case}
            my_dict.update(my_entry)
            print("Checking inventory, if this item with item code {} already exists..... ".format(item_serial_code))
            print(f"{item_name} with {item_serial_code} is not in inventory.... ")
            print("Add new item {} having {} in the inventory....".format(item_name,item_serial_code))
            separate_enteries()
            if os.path.exists(filename):
                with open( filename, 'w') as f:
                    f.write(str(my_dict)+"\n")
    return my_dict

def display(my_dict):
    if not my_dict:
        print("Inventory does not have any item to display....")
        separate_enteries()
    else:
        separate_enteries()
        full_name,student_number=display_my_info()
        print(full_name,"\n",student_number+"\n")
        separate_enteries()

        print("%30s%30s%30s%30s"%("Item Name","Serial Code","Item Quantity in stock","Price Per item"))

        # for key in my_dict.keys():
        #     print(my_dict[key]["Item name"])
        for key,value in my_dict.items():
            itm_nm = value["Item name"]
            serial_code = value["Serial code"]
            qty = value["Qty per item"]
            price = round(value["Price per unit"],2)

            print("%30s%30s%30s%30s"%(itm_nm,serial_code,qty,"$"+str(price)))
        separate_enteries()

def search_based_on_serial_code(my_dict,serial_no):

    # serial_no = input("Please enter serial code to search:"+"\t\t")
    
    if any(serial_no in x.values() for x in  my_dict.values()):
        for k,v in my_dict.items():
            if serial_no in v["Serial code"]:
                print("Item exist in the inventory")
                separate_enteries()
                full_name,student_number=display_my_info()
                print(full_name,"\n",student_number+"\n")
                separate_enteries()
                print("%30s%30s%30s%30s"%("Item Name","Serial Code","Quantity Per Item","Price Per unit"))
                print("%30s%30s%30s%30s"%(v["Item name"],v["Serial code"],v["Qty per item"],round(v["Price per unit"],2)))
                separate_enteries()
   

    elif not any(serial_no in x.values() for x in  my_dict.values()):
        print(f"Item having item serial code {serial_no} is not currently in inventory")
        separate_enteries()     

def enter_item_info():

    item_name = input("Please enter item name:\t\t")
    item_serial_code =  input("Please enter serial code:\t\t")
    qty_per_item = int(input("Please enter quantity of items:\t\t"))
    price_per_unit = float(input("Please enter price per unit:\t\t$"))

    return item_name,item_serial_code,qty_per_item,price_per_unit


def send_email(temp_dict,total_price,total_tax,total_paid):
                
    with open('config.json', 'r') as f:
        my_pass = json.load(f)

    password = my_pass.get('password')

    EMAIL_ADDRESS = 'hanieh.miii@gmail.com'
    EMAIL_PASSWORD = 'zfehtbjnohprzmzf'
    msg = EmailMessage()
    msg['Subject'] = 'My Sales Invoice - todate'
    msg['From'] = EMAIL_ADDRESS 
    msg['To'] = EMAIL_ADDRESS

    table_rows = ""
    for k,v in temp_dict.items():
        table_rows += f"<tr><td>{v['My date']}</td><td>{v['Item name']}</td><td>{v['Serial code']}</td><td>{v['Qty per item']}</td><td>${v['Price per unit']}</td></tr>"

    msg.add_alternative(f"""\n\n\
    <html>
        <head>
        <style type="text/css">
            .tg  {{border-collapse:collapse;border-spacing:0;}}
            .tg td{{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border:1px solid black; margin: 0 auto;text-align: right !important; }}
            .tg th{{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border:1px solid black;font-weight: bold; }}
            .td test{{text-align: right !important; }}
            .tg .tg-0lax{{text-align:left;vertical-align:top}}
        </style>
        </head>
        <body>
        <h1 style={{left:120px}}>Sale Invoice</h1>
        <p>****************************************************************************************************************************</p>
        
        <table class="tg">
            <tr>
            <th class="tg-0lax">Time of sale</th>
            <th class="tg-0lax">Item Name</th>
            <th class="tg-0lax">Item Serial ID</th>
            <th class="tg-0lax">Item quantity in stock</th>
            <th class="tg-0lax">Price per item</th>
            </tr>
            {table_rows}

            <td class="tg-0lax" colspan="4" >Total price for all items purchased</td>
                <td class="tg-0lax">${str(round(total_price,2))}</td>
            </tr>
                <tr>
                <td class="tg-0lax" colspan="4">Tax amount paid</td>
                <td class="tg-0lax">${str(round(total_tax,2))}</td>
            </tr>
            </tr>
                <tr>
                <td class="tg-0lax" colspan="4" >Total amount paid</td>
                <td class="tg-0lax">${str(round(total_paid,2))}</td>
            </tr>
        </table>

        <p>****************************************************************************************************************************</p>

        </body>
        </html>
    """,subtype="html")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
        smtp.send_message(msg)


def display_date():
    now = datetime.now().time().strftime("%H:%M:%S") # time object
    date = datetime.now().strftime("%Y-%m-%d") # date object
    my_date = date+ " at "+now
    return my_date


def display_sale_info(mydict,temp_dict,qty_to_purhcase,i):
    separate_enteries()
    full_name,student_number=display_my_info()
    print(full_name,"\n",student_number+"\n")
    separate_enteries()                           
    print(" "*55 + "Sales Invoice")
    print("%24s%24s%24s%24s%24s"%("Time of Sale","Item Name","Serial Code","Quantity Per Item","Price Per unit"))
    itm_nm = mydict[i]["Item name"]
    serial_code = mydict[i]["Serial code"],
    price_per = round(mydict[i]["Price per unit"],2)
    my_date=display_date()
    str_serial_code = ' '.join(serial_code)
    new_case = {
        "My date":my_date,
        "Item name":itm_nm,
        "Serial code":str_serial_code,
        "Qty per item":qty_to_purhcase,
        "Price per unit":price_per
    }
    temp_dict.update({len(temp_dict)+1:new_case})
    for k,v in temp_dict.items():
        print("%24s%24s%24s%24s%24s"%(v["My date"],v["Item name"],v["Serial code"],v["Qty per item"],"$"+str(v["Price per unit"])))
    separate_enteries()


def sales(mydict,temp_dict,itm_for_sale,qty_to_purhcase):

    item_found = False
    l = []
    for i in mydict:
        if mydict[i]["Serial code"] == itm_for_sale:
            item_found=True
            if mydict[i]["Qty per item"] < qty_to_purhcase:
                print("Not enough quantity in stock... ... ...")
                print("There are no invoices in the system yet... ... ...")
            elif qty_to_purhcase < mydict[i]["Qty per item"]:

                sales = display_sale_info(mydict,temp_dict,qty_to_purhcase,i)
                total_price = qty_to_purhcase*mydict[i]["Price per unit"]
                print("%90s%30s"%("Total price for all items purchased","$"+str(round(total_price,2))))
                total_tax = total_price * 0.13
                print("%90s%30s"%("Tax amount paid","$"+str(round(total_tax,2))))
                total_paid = total_price+total_tax
                print("%90s%30s"%("Total amount paid","$"+str(round(total_paid,2))))
                updated_qty = mydict[i]["Qty per item"] - qty_to_purhcase
                mydict[i]["Qty per item"] = updated_qty

                send_email(temp_dict,total_price,total_tax,total_paid)

            elif qty_to_purhcase == mydict[i]["Qty per item"]:  
                
                #second way
                # my_dict_copy = {key: value for key, value in my_dict.items() if value["Qty per item"] != qty_to_purhcase}
                # my_dict = my_dict_copy

                for k,v in mydict.items():
                    if v["Serial code"] == itm_for_sale:
                        l.append(k)

                sales = display_sale_info(mydict,temp_dict,qty_to_purhcase,i)
                total_price = qty_to_purhcase*mydict[i]["Price per unit"]
                print("%90s%30s"%("Total price for all items purchased","$"+str(round(total_price,2))))
                total_tax = total_price * 0.13
                print("%90s%30s"%("Tax amount paid","$"+str(round(total_tax,2))))
                total_paid = total_price+total_tax
                print("%90s%30s"%("Total amount paid","$"+str(round(total_paid,2))))
                updated_qty = mydict[i]["Qty per item"] - qty_to_purhcase
                mydict[i]["Qty per item"] = updated_qty

                send_email(temp_dict,total_price,total_tax,total_paid)
                print(f"Item with {mydict[i]['Serial code']} is now out of stock and removed from inventory. ")


    for i in l:
        del mydict[i]

    if item_found == False:
        print("Item not in stock ... ... ... Please connect later ... ... ...")
        print("There no invoices in the system yet ... ... ...")
        
    return mydict,temp_dict


def main():
    print(__doc__)
    my_dict = {}
    temp_dict = {}

    full_name, student_number = display_my_info()
    print(full_name,"\n",student_number)
    separate_enteries()
    
    filename =my_filename()
    txt = Path(filename).read_text()
    # print(txt[0])
    #if txt file is not empty
    if os.path.getsize(filename) > 1:
        # txt.replace(txt[0],"")
        # txt.replace(txt[-2],"")
        my_dict = txt
        #convert str to dictionary
        my_dict = ast.literal_eval(my_dict)

    while True:
        choice = display_info()
        if(choice == "1"):                    
            my_dic_length = len(my_dict)
            add_items(my_dict)

        elif(choice == "2"):
            display(my_dict)
            
        elif(choice == "3"):
            
            if len(my_dict)==0:
                print("There are no item in the dictionary to display....")
                separate_enteries()
            else:
                serial_no = input("Please enter serial code to search:"+"\t\t")
                search_based_on_serial_code(my_dict,serial_no)
        elif(choice=="4"):
            
            if len(my_dict)  == 0:
                print("No items in the inventory for sale.")
            else:
                itm_for_sale = input("Enter item serial code of item to purhase:\t ")
                # qty_to_purhcase = input("Quantity of items having serial number {} to buy").format(itm_for_sale)
                qty_to_purhcase = int(input(f"Quantity of items having serial number {itm_for_sale} to buy:\t"))
                my_dict,temp_dict = sales(my_dict,temp_dict,itm_for_sale,qty_to_purhcase)

                #update the dictionary in the file
                if os.path.exists(filename):
                    with open( filename, 'w') as f:
                        f.write(str(my_dict)+"\n")
            separate_enteries()
        elif(choice == "5"):
            print("Application ending...")
            break
        elif(choice != 1 or choice != 2 or choice != 3 or choice !=4):
            print("Please enter a valid choice....\n")
            separate_enteries()
        else:
            print("Enter a valid choice .... .... ....")
            separate_enteries()
            continue
main()

# if __name__ == "__main__":
#     main()
