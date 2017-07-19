import csv
import getpass #from stackoverflow thread

uid = getpass.getuser() #from stackoverflow thread
products = "C:\users\zappari\desktop\python_class\crud_app\data\products.csv"

def lookup(pid):
    return

with open(products, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)
    row_count = len(data)


print "\n", "Welcome", uid, "\n"

print "There are ", row_count, " products in the database.  Please select an operation:\n"

print """
operation         |   description
---------------   |   ---------------
List              |   Display a list of product identifiers and names
Show              |   Show information about a product
Create            |   Add a new product
Update            |   Edit an existing product
Destroy           |   Delete an existing product

"""

user_input = raw_input("Operation Selection:")

if user_input.title() == "List":
    for row in data:
        print " + ", row["id"], row["name"], row["price"], row["department"]
        #for key, value in row.iteritems() :
            #print key, value
        #print row
elif user_input == "Show":
    show_param = raw_input("Please input the ID number for the product you'd like to review:")

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
