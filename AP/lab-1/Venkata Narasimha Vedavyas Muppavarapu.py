'''
*****************************************************************************************************************************
                                                       My car dealership
*****************************************************************************************************************************

This application is used by a car dealership to determine inventory value in stock. This dealership has two different make of vehicles in inventory.
They (car dealership) keep the most popular colour that their customers choose. So each vehicle make has its own popular colour.
This application shows total number of vehicles in the inventory, total price of vehicles in the inventory,
amount of tax paid on the inventory and the total worth of inventory in stock.
Application asks user to enter vehicle make - user enters vehicle make (String type)
Application asks user to enter vehicle color - user enters vehicle color (String type)
Application asks user to enter number of vehicles - user enters vehicle number (integertype)
Application asks user to enter price per vehicle - user enters price per vehicle (float type)
Application then asks the same questions for the second vehicle
Application asks user to enter second vehicle make - user enters vehicle make (String type)
Application asks user to enter second vehicle make color - user enters vehicle color (String type)
Application asks user to enter number of vehicles (second make) - user enters vehicle number (integer type)
Application asks user to enter price per vehicle (of second make) - user enters price per vehicle (float type)

After data is entered, application then displays the following output:

                                                                                            Dealership name: <your name>
                                                                                    Dealership code: <your student number>

Vehicle make                Vehicle color               Number of vehicles              Price per vehicle
<vehicle make 1 name >      <vehicle make 1 color>      <number of vehicles make 1>     <price per vehicle of make 1>
<vehicle make 2 name >      <vehicle make 2 color>      <number of vehicle make 2>      <price per vehicle of make 2>

                                                                                Total vehicles in dealership: <number>
                                                                                    Total inventory amount: <$amount>
                                                                             Total tax amount that is paid: <$amount>
                                                                            Total inventory amount and taxes: <$amount>

*****************************************************************************************************************************
'''

#input student name and ID
name = input("Enter your name:\t\t")
student_Id = input("Enter your student ID:\t\t")

#Maker1 Details i.e brand name of the maker, color of vehicle, no of units present in inventory, price per unit of vehicle
vehicle_maker1_name = input("Enter vehicle first brand of vehicle make:\t\t")
vehicle_color_of_maker1_name = input("Enter color of first brand (amke) of vehicles:\t\t")
vehicle_quantity_of_maker1 = int(input("Enter quantity of first brand (make) of vehicles:\t\t"))
price_per_vehicle_from_maker1_of_vehicles = float(input("Enter price per vehicle for the first brand (make) of vehicles:\t\t$"))

#Maker2 Details i.e brand name of the maker, color of vehicle, no of units present in inventory, price per unit of vehicle
vehicle_maker2_name = input("Enter vehicle second brand of vehicle make:\t\t")
vehicle_color_of_maker2_name = input("Enter color of second brand (amke) of vehicles:\t\t")
vehicle_quantity_of_maker2 = int(input("Enter quantity of second brand (make) of vehicles:\t\t"))
price_per_vehicle_from_maker2_of_vehicles = float(input("Enter price per vehicle for the second brand (make) of vehicles:\t\t$"))

#Calculating total vehicles in dealership including all makers we have
total_vehicles_in_dealership = vehicle_quantity_of_maker1 + vehicle_quantity_of_maker2

#Calculating price(inventory amount) of vehicles in dealership from each vehicle maker1, maker2
inventory_amount_of_vehicle_maker1 = vehicle_quantity_of_maker1 * price_per_vehicle_from_maker1_of_vehicles
inventory_amount_of_vehicle_maker2 = vehicle_quantity_of_maker2 * price_per_vehicle_from_maker2_of_vehicles

#total inventory amount from vehicle makers
total_inventory_amount_of_vehicles_maker1_and_maker2 = inventory_amount_of_vehicle_maker1 + inventory_amount_of_vehicle_maker2
total_inventory_amount_of_vehicles_maker1_and_maker2_str = "Total Inventory Amount:     $%.2f"%(total_inventory_amount_of_vehicles_maker1_and_maker2)

#Calculation of tax for each makers based on inventory amount, and total tax of both vehicle makers
tax_amount_of_vehicle_maker1 = 0.13 * inventory_amount_of_vehicle_maker1
tax_amount_of_vehicle_maker2 = 0.13 * inventory_amount_of_vehicle_maker2
total_tax_amount_of_vehicles_maker1_and_maker2 = tax_amount_of_vehicle_maker1 + tax_amount_of_vehicle_maker2
total_tax_amount_of_vehicles_maker1_and_maker2_str = "Total tax amount that is paid:    $%.2f"%(total_tax_amount_of_vehicles_maker1_and_maker2)

#calculation of total amount including taxes and inventory amount
total_inventory_amount_and_taxes_of_vehicle_maker1_and_maker2 = total_inventory_amount_of_vehicles_maker1_and_maker2 + total_tax_amount_of_vehicles_maker1_and_maker2
total_inventory_amount_and_taxes_of_vehicle_maker1_and_maker2_str = "Total inventory amount and taxes:    $%.2f"%(total_inventory_amount_and_taxes_of_vehicle_maker1_and_maker2)

#displaying name and student ID in heading

display_name_ID_head = "%120s\n"%(name)
display_name_ID_head += "%120s\n\n"%(student_Id)

#display heading

display_header ="%30s%30s%30s%30s\n"%("Vehicle make","Vehicle color","Number of vehicles","Price per Vehicle")
display_info = "%30s%30s%30s%30s\n\n"%(vehicle_maker1_name,vehicle_color_of_maker1_name,vehicle_quantity_of_maker1,"$%.2f"%(price_per_vehicle_from_maker1_of_vehicles))
display_info += "%30s%30s%30s%30s\n\n"%(vehicle_maker2_name,vehicle_color_of_maker2_name,vehicle_quantity_of_maker2,"$%.2f"%(price_per_vehicle_from_maker2_of_vehicles))
display_info += "%120s\n"%("Total vehicles in dealership:             "+str(total_vehicles_in_dealership))
display_info += "%120s\n%120s\n%120s\n"%(total_inventory_amount_of_vehicles_maker1_and_maker2_str, total_tax_amount_of_vehicles_maker1_and_maker2_str, total_inventory_amount_and_taxes_of_vehicle_maker1_and_maker2_str)


#Display the information report
print('*' * 125)
print(' ' * 55 + "My car dealership")
print('*' * 125)
print(display_name_ID_head)
print(display_header)
print(display_info)
print('*' * 125)