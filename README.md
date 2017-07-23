# Product inventory application

This app executes CRUD operations on a product inventory of a specified structure stored as a csv file to be located in the data subfolder of the crud app parent directory.  THe app will read in the initial product inventory from the csv file, and will update that file based on the selected operations executed within the app.  Operations options are:
-List: all files currently in the invetory
-Show: display detailed view of one record specified by user input product ID
-Create: create a new product entry to be added to the inventory
-Update: edit product information for an existing product in the inventory
-Destroy: delete a product record from the inventory

## Installation

Download the source code:

```shell
git clone https://github.com/rjzap/crud_app_project.git
cd some/path/to/repo/
```

Finally, download the [example `products.csv` file](https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-70-201706/master/projects/crud-app/products.csv) and save it as `data/products.csv`.

## Usage

```shell
python app/products_app.py
```
