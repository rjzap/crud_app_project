import csv
import getpass #from stackoverflow thread
import itertools
from collections import OrderedDict as od
from operator import itemgetter

uid = getpass.getuser() #from stackoverflow thread
csv_file_path = "data/products.csv"

products = []

#READ INVENTORY CSV FILE

with open(csv_file_path, "r") as csv_file:
  reader = csv.DictReader(csv_file)
  for row in reader:
    products.append(row)

row_count = len(products)

def show_lookup(show_param):
    return [p for p in products if p['id'] == show_param]

def create_prod():
    print "To create a new product, please specify the product's information..."
    product_id = int(products[-1]["id"]) + 1
    product_name = raw_input("Product Name is:")
    product_dep = raw_input("Product department is:")
    product_aisle = raw_input("Product aisle is:")
    product_price = raw_input("Product price is:")
    new_product = {
        'id' : product_id,
        'name' : product_name,
        'department' : product_dep,
        "aisle" : product_aisle,
        "price" : product_price
        }
    print "The new product is:\n", new_product
    products.append(new_product)

def update_prod(upd_param):
    upd_ind = map(itemgetter("id"), products).index(upd_param)
    for k in disp_key_order[1:]:
        products[upd_ind][k] = raw_input("Change product " + k + " from " + ' "{}"'.format(products[upd_ind][k]) + " to: ")

def destroy_prod():
    destr_param = raw_input("Please specify the product ID for the record you'd like to delete:")
    prod_elim = [p for p in products if p['id'] == destr_param]
    print "Destroying", prod_elim      



print "\n", "Welcome", uid, "\n"

print "There are {0} products in the database.  Please select an operation:\n".format(row_count)

print """
operation         |   description
---------------   |   ---------------
List              |   Display a list of product identifiers and names
Show              |   Show information about a product
Create            |   Add a new product
Update            |   Edit an existing product
Destroy           |   Delete an existing product

"""



if select_op == "List":
    for row in products:
        print " + ", row["id"], row["name"], row["department"] , row["aisle"], disp_price
elif select_op == "Show":
    show_param = raw_input("Please input the product ID for the product record like to review:")
    show_dis = show_lookup(show_param)[0]
    show_display = od((k, show_dis[k]) for k in disp_key_order)
    for k, v in show_display.iteritems():
        print " + ", k.title(), ": ", v
elif select_op == "Create":
    create_prod()
elif select_op == "Update":
    upd_param = raw_input("Please specify the product ID for the product record you'd like to edit:")
    update_prod(upd_param)
elif select_op == "Destroy":
    destroy_prod()



#elif user_input == "Update":
#    print "Edit an existing product"
#elif user_input == "Destroy":
#    print "Delete an existing product"
#else:
#    print "Please type a recognized operation from the menu options"

#w_file_path =  "C:\users\zappari\desktop\python_class\crud_app\data\write_practice.csv"

#with open(w_file_path, "w") as csv_file:
#    writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
#    writer.writeheader() # uses fieldnames set above
#    for row in data:
#        writer.writerow(row)

with open(csv_file_path, "wb") as csv_file:
  writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
  writer.writeheader() # uses fieldnames set above
  for product in products:
    writer.writerow(product)


#menu = {}
#menu['1']="List"
#menu['2']="Show"
#menu['3']="Create"
#menu['4']="Update"
#menu['5']="Destroy"
#while True:
#  options=menu.keys()
#  options.sort()
#    for entry in options:
#      print entry, menu[entry]

#    selection=raw_input("Please Select:")
#    if selection =='1':
#      print "add"
#    elif selection == '2':
#      print "delete"
#    elif selection == '3':
#      print "find"
#    elif selection == '4':
#      break
#    else:
#      print "Unknown Option Selected!"
