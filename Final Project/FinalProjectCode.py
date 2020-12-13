# Name: Dang Nguyen
# Student Id: 1861688
# Final Project
import csv
from datetime import *

complete_dict = {}
complete_list = []
item_type_dict = {}

# Reading data from Manufactures List csv file and storing in required data structures
def process_manufacturer_list():
	# print("\nManufacturer List:")
	with open('ManufacturerList.csv') as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    line_count = 0
	    for row in csv_reader:
	    	# print(row)
	    	id_ = row[0]
	    	manufacturer = row[1]
	    	item = row[2]
	    	damaged = row[3]
	    	complete_dict[id_] = {
	    		"manufacturer": manufacturer,
	    		"item": item,
	    		"damaged": damaged
	    	}

# Reading data from Price List csv file and storing in required data structures
def process_price_list():
	# print("\nPrice List:")
	with open('PriceList.csv') as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    line_count = 0
	    for row in csv_reader:
	    	# print(row)
	    	id_ = row[0]
	    	price = row[1]
	    	obj = complete_dict[id_]
	    	obj["price"] = price
	    	complete_dict[id_] = obj

# Reading data from Service Date List csv file and storing in required data structures
def process_serviceDate_list():
	# print("\nService Date List:")
	with open('ServiceDatesList.csv') as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    line_count = 0
	    for row in csv_reader:
	    	# print(row)
	    	id_ = row[0]
	    	date = row[1]
	    	obj = complete_dict[id_]
	    	obj["date"] = date
	    	complete_dict[id_] = obj

# Creating full inventory list which would be used in further processes
def create_full_inventory_list():
	for x in complete_dict:
		# print(x)
		list_ = []
		list_.append(x)
		# for val in complete_dict[x].values():
		# 	list_.append(val)
		list_.append(complete_dict[x]["manufacturer"])
		list_.append(complete_dict[x]["item"])
		list_.append(complete_dict[x]["price"])
		list_.append(complete_dict[x]["date"])
		list_.append(complete_dict[x]["damaged"])
		complete_list.append(list_)

# Writing full inventory list in FullInventory.csv file
def write_full_inventory_file():
	file = open('FullInventory.csv', 'w+', newline ='') 
	with file:     
	    write = csv.writer(file) 
	    write.writerows(complete_list)

# Creating seperate lists for each type of item
def bisect_list_by_item():
	for x in complete_list:
		item = x[2]
		id_ = x[0]
		manufacturer = x[1]
		price = x[3]
		date = x[4]
		damaged = x[5]
		list_ = [id_, manufacturer, price, date, damaged]
		if item in item_type_dict:
			# If any data is present of this type of item
			current_item_list = item_type_dict[item]
			current_item_list.append(list_)
			item_type_dict[item] = current_item_list
		else:	
			item_type_dict[item] = [list_]

# Writing data to csv file for each type of item
def create_item_type_inventory_list():
	for x in item_type_dict:
		# It will make the first letter of string as capital letter
		item_name = x.capitalize()
		# Sorting the list acccording to item id
		item_type_dict[x].sort()
		list_ = item_type_dict[x]
		# print(item_name, list_)
		filename = item_name + "Inventory.csv"
		file = open(filename, 'w+', newline ='') 
		with file:     
		    write = csv.writer(file) 
		    write.writerows(list_)

# Writing data of those items whose service date are before the current date
def create_past_service_date_inventory():
	# Storing present date
	d = date.today()
	# print(d)
	answer_list = []
	for x in complete_list:
		y = x.copy()
		date_ = x[4]
		date_ = date_.split('/')
		month = date_[0]
		day = date_[1]
		year = date_[2]
		# Formatting date to compare it with today's date
		date_ = date(int(year), int(month), int(day))
		if(date_ < d):
			# If current date is newer than item's service date
			y[4] = date_
			answer_list.append(y)
	# Sorting the answer list acccording to date
	answer_list.sort(key=lambda x: x[4])
	# print(answer_list)
	for x in answer_list:
		day = x[4].day
		month = x[4].month
		year = x[4].year
		# print(month, day, year)
		# Formatting the date again in original format
		x[4] = str(month) + "/" + str(day) + "/" + str(year)
	file = open("PastServiceDateInventory.csv", 'w+', newline ='') 
	with file:     
	    write = csv.writer(file) 
	    write.writerows(answer_list)

# Storing the items which are damaged
def create_damaged_inventory():
	answer_list = []
	for x in complete_list:
		if x[5] != '':
			y = x.copy()
			# Removing the damaged/undamaged column from the list
			y.pop()
			answer_list.append(y)
	# Sorting the list accordin to price
	answer_list.sort(key=lambda x: x[3])
	answer_list.reverse()
	file = open("DamagedInventory.csv", 'w+', newline ='') 
	with file:     
	    write = csv.writer(file) 
	    write.writerows(answer_list)

# To compare input date to this function with the current date
def check_date(date_):	
	d = date.today()
	date_ = date_.split('/')
	month = date_[0]
	day = date_[1]
	year = date_[2]
	date_ = date(int(year), int(month), int(day))
	if(date_ > d):
		return True
	else:
		return False

# To check if this item is present in the inventory
def check_item(input_string):
	# Creating a item set for all the different items
	item_set = []
	for x in complete_list:
		item_set.append(x[2].lower().strip())
	item_set = set(item_set)

	# Creating a manufacturer set for all the different manufacturers
	manufacturer_set = []
	for x in complete_list:
		manufacturer_set.append(x[1].lower().strip())
	manufacturer_set = set(manufacturer_set)

	# print(item_set, manufacturer_set)

	# Splitting input string in different words
	input_string = input_string.split(' ')
	# Storing count of items and manufacturers in the input string
	item_ct = 0
	manufacturer_ct = 0
	user_item = ''
	user_manufacture = ''

	# for each word in input string
	for x in input_string:
		# performing case insensitive search
		if x.lower() in item_set:
			item_ct = item_ct + 1
			user_item = x
		if x.lower() in manufacturer_set:
			manufacturer_ct = manufacturer_ct + 1
			user_manufacture = x

	# If no item is found or no manufacturer is found or more than 1 item or more than 1 manufacturer is found
	if item_ct == 0 or manufacturer_ct == 0 or item_ct > 1 or manufacturer_ct > 1:
		print("No such item in inventory!")
		return

	# Getting all possible data from the inventory with this combination of item and manufacturer
	possible_items = []
	for x in complete_list:
		if x[1].lower().strip() == user_manufacture.lower() and x[2].lower().strip() == user_item.lower():
			# Item should not be damaged and service date should not be expired
			if x[5] == '' and check_date(x[4]):
				possible_items.append(x)

	# Sorting the possible items according to price
	possible_items.sort(key=lambda x: x[3])
	possible_items.reverse()

	if len(possible_items) == 0:
		print("No such item in inventory!")
		return
	else:
		# Printing the required item details
		item = possible_items[0]
		print("Your item is -  ID:", item[0], "Manufacturer:", item[1], "Item:", item[2], "Price:", item[3])


	# Getting details of same type of item from other manufacturers
	also_consider_items = []
	for x in complete_list:
		if x[1].lower().strip() != user_manufacture.lower() and x[2].lower().strip() == user_item.lower():
			# Item should not be damaged and service date should not be expired
			if x[5] == '' and check_date(x[4]):
				also_consider_items.append(x)

	if len(also_consider_items) != 0:
		print("You may, also, consider:")
		for x in also_consider_items:
			print("ID:", x[0], "Manufacturer:", x[1], "Item:", x[2], "Price:", x[3])


print("-----------------------------------")
print("Program Started")
# Reading data from Manufactures List csv file and storing in required data structures
process_manufacturer_list()
# Reading data from Price List csv file and storing in required data structures
process_price_list()
# Reading data from Service data List csv file and storing in required data structures
process_serviceDate_list()

# Creating Full Inventory list for further usage
create_full_inventory_list()

# Sorting the list by manufacturer name
complete_list.sort(key=lambda x: x[1])
# print(complete_list)
# Writing the sorted list in csv file
write_full_inventory_file()

# Creating seperate lists for each item
bisect_list_by_item()
# print(item_type_dict)
# Writing seperate lists for each item in respective csv files
create_item_type_inventory_list()

# Writing data to a csv file is item's service data is expired
create_past_service_date_inventory()

# Writing damages items data in a csv file
create_damaged_inventory()
print("-----------------------------------")
print("Created all inventory csv files")

while 1 == 1:
	print("-----------------------------------")
	user_input = input("\nEnter the manufacturer and item type, or q to quit\n")
	if user_input == "q":
		# If user chooses to quit
		break
	# checking if entered item is present in inventory
	check_item(user_input)

print("\n-----------------------------------")
print("Program Ended")