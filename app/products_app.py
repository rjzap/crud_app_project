import csv
import getpass #from stackoverflow thread

uid = getpass.getuser() #from stackoverflow thread
products = "C:\users\zappari\desktop\python_class\crud_app\data\products.csv"

with open(products, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)
    row_count = len(data)


def show_lookup(show_param):
    return [p for p in data if p['id'] == show_param]

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

user_input = raw_input("Operation Selection:").title()

if user_input.title() == "List":
    for row in data:
        print " + ", row["id"], row["name"], row["price"], row["department"]
elif user_input == "Show":
    show_param = raw_input("Please input the ID number for the product you'd like to review:")
    show_display = show_lookup(show_param)[0]
    print " + Prodcut ID: ", show_display['id']
    print " + Name: ", show_display['name']
    print " + Department: ", show_display['department']
    print " + Aisle: ", show_display['aisle']
    print " + Price: ", '${0:.2f}'.format(float(show_display['price']))
elif user_input == "Create":
    print "Add a new product"
elif user_input == "Update":
    print "Edit an existing product"
elif user_input == "Destroy":
    print "Delete an existing product"
else:
    print "Please type a recognized operation from the menu options"


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
