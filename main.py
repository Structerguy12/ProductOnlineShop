import pickle

try:
    with open("products.pickle", "rb") as file:
        products = pickle.load(file)
except:
    products = {}

def AddProduct():
    Product = input("Please product: ")
    Price = float(input("Please price of your product " + Product + ": "))
    products[Product] = Price
def DeleteProduct():
    Delete = input("Please select product you want to delete: ")
    if Delete in products:
        products.pop(Delete)
        print("Item has been succesfully deleted.")
    else:
        print("Item hasn't been found in the products. Please try again.")

def DisplayProducts():
    for i, j in products.items():
        print(f"{i} price {j}")
def ProductSearch():
    ProductSearchBar = input("Please select product you want to view: ")
    if ProductSearchBar in products:
        print("The price of product "+ProductSearchBar+ " is "+str(products[ProductSearchBar])+".")

def ChangeProductPrice():
    ProductPriceChanger= input("Please select product you want to change the price of: ")
    if ProductPriceChanger in products:
        ProductPriceChanger2 = float(input("Please price: "))
        products[ProductPriceChanger] = ProductPriceChanger2
        print("Has been succesfully changed!")
    else:
        print("Product doesn't exist. Try again")
while True:
    print("Use command ;AddProduct to add a product to the current products")
    print("Use command ;DeleteProduct which will delete the product you entered")
    print("Use command ;DisplayProducts which will display all products")
    print("Use command ;GetProduct which will display a product that you picked")
    print("Use command ;ChangeProductPrice which will let you change the price of a product")
    Command = input("Please command --> ")
    if Command == ";AddProduct":
        AddProduct()
    elif Command == ";DeleteProduct":
        DeleteProduct()
    elif Command == ";DisplayProducts":
        DisplayProducts()
    elif Command == ";GetProduct":
        ProductSearch()
    elif Command == ";ChangeProductPrice":
        ChangeProductPrice()
    else:
        print("That command doesn't exist. Please try again")
    with open("products.pickle", "wb") as file:
        pickle.dump(products, file)
