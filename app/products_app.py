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

def prod_list():
    for row in products:
        disp_price = '${0:.2f}'.format(float(row['price']))
        print " + ", row["id"], "|", row["name"], "|", row["department"], "|", row["aisle"], "|", disp_price

def show_lookup():
    show_param = raw_input("\nPlease input the product ID for the product record you'd like to review: ")
    prod_lkup = products
    prod_lkup = [p for p in products if p['id'] == show_param]
    show_dis = prod_lkup[0]
    show_display = od((k, show_dis[k]) for k in disp_key_order)
    print ""
    for k, v in show_display.iteritems():
        print " + ", k.title(), ": ", v

def create_prod():
    print "\nTo create a new product, please specify the product's information...\n"
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
    print "\nThe new product is:\n", new_product
    products.append(new_product)

def update_prod():
    upd_param = raw_input("\nPlease specify the product ID for the product record you'd like to edit:")
    upd_ind = map(itemgetter("id"), products).index(upd_param)
    for k in disp_key_order[1:]:
        products[upd_ind][k] = raw_input("\nChange product " + k + " from " + ' "{}"'.format(products[upd_ind][k]) + " to: ")

def destroy_prod():
    global products
    destr_param = raw_input("\nPlease specify the product ID for the record you'd like to delete:")
    prod_elim = [p for p in products if p['id'] == destr_param]
    prod_elim = od((k,prod_elim[0][k]) for k in disp_key_order)
    print "\nDestroying: \n"
    for k,v in prod_elim.iteritems():
        print " + ", k.title(), ": ", v
    products = [p for p in products if p['id'] != destr_param]

print "-----------------------------"
print "PRODUCT INVENTORY APPLICATION"
print "-----------------------------"

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

disp_key_order = ("id", "name", "department", "aisle", "price")
select_op = raw_input("\nType desired operation from menu list options:").title()

if select_op == "List":
    prod_list()
elif select_op == "Show":
    show_lookup()
elif select_op == "Create":
    create_prod()
elif select_op == "Update":
    update_prod()
elif select_op == "Destroy":
    destroy_prod()
else:
    print "Please input a recognized operation from the menu"

##WRITE INVENTORY CSV FILE

with open(csv_file_path, "wb") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)
