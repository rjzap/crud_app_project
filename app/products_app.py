import csv
import getpass #from stackoverflow thread

uid = getpass.getuser() #from stackoverflow thread
db = "C:\users\zappari\desktop\python_class\crud_app\data\products.csv"

with open(db, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)
    row_count = len(data)
#    for row in reader:
#        print(row["name"], row["price"])

print "Welcome", uid, "\n"

print "There are ", row_count, " products in the database.  Please select an operation:\n"

print "operation         |   description"
print "---------------   |   ---------------"
print "List              |   Display a list of product identifiers and names"
print "Show              |   Show information about a product"
print "Create            |   Add a new product"
print "Update            |   Edit an existing product"
print "Destroy           |   Delete an existing product"

#user_input = raw_input("Please input a valid product idenitifer, or 'DONE' if there are no more items:")
#if user_input == "DONE":
#    break
#else:
#    product_ids.append(int(user_input))

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
