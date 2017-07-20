import csv
import getpass #from stackoverflow thread
import itertools

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

def create_prod(create_param):
    print "To create a new product, please specify the product's information..."
    product_name = raw_input("Product Name is:")
    product_aisle = raw_input("Product aisle is:")
    new_product = {
        'id':product_id, 'name': product_name}
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

select_op = raw_input("Operation Selection:").title()
disp_price = '${0:.2f}'.format(float(row['price']))

if select_op == "List":
    for row in products:
        print " + ", row["id"], row["name"], disp_price, row["department"]
elif select_op == "Show":
    show_param = raw_input("Please input the ID number for the product you'd like to review:")
    show_display = show_lookup(show_param)[0]
#    print " + Product ID: ", show_display['id']
#    print " + Name: ", show_display['name']
#    print " + Department: ", show_display['department']
#    print " + Aisle: ", show_display['aisle']
#    print " + Price: ", '${0:.2f}'.format(float(show_display['price']))
    for k, v in show_display.iteritems():
        print " + ", k.title(), ": ", v
elif user_input == "Create":
    print "Add a new product"


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
