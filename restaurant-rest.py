# This Program checks the booking data for availability of tables, takes the customer order in a restaurant
# and generates the bill to the customer.Finally gets the rating of the service from the customer.

# Key Features Demonstrated :
# 1. Classes / Objects
# 2. Docstrings
# 3. File Handling
# 4. Error and Exception Handling
# 5. Data Structures - Dictionaries
# 6. lambda function
# 7. String Manipulation

# Imports from standard library
import datetime
import time
import sys

print("WELCOME TO QUICKCONNECT HUB")

class Restaurant:

    order = {}
    total = 0.0
    tax = 0.04

    def __init__(self):
        """ Read / Display restaurant table booking information stored in a file """

        print("\n" "Displaying Table Booking Data ...." "\n")
        time.sleep(2)
                
        try:

           with open("table.txt","r") as tabfile:

               for line in tabfile:
                  print(line)
               time.sleep(2)

               print("\n" "Please occupy empty table")
               time.sleep(2)

        except FileNotFoundError:
           print("The data file is missing")
           sys.exit()

    def menuDisplay(self):
        """ Display the items in the menu for selection """
        
        print("\n" "Select the items from menu")
        print("\n" "********** MENU CARD **********")
        print("ITEM \t\t PRICE")

        self.menu = {"Burger":120, "Pizza":200, "Hotdog":150,
                "Parata":50, "Donut":80, "Nugget":50,
                "Paneer":120, "Pakora":80, "Coffee":25}

        for k,v in self.menu.items():
              print(k,":", "\t",  "Rs",v)

    def orderConfirm(self):
        """ Take the order and display the items for confirmation """

        print("\n" "Please let us know the order")
        time.sleep(2)

        for i in range(len(self.menu)):
            
            self.select_item = input("\n" "Select an Item: ")
            if self.select_item not in self.menu:
                print("Selected item is not available in the menu")
                self.select_item = input("Please re-enter an item: ")
                
            try:
                self.quantity = int(input("Enter the Quantity: "))
                self.order[self.select_item] = self.quantity

            except Exception:
                print("Quantity to be entered as Numeric")
                self.quantity = int(input("Please re-enter the Quantity:"))
                self.order[self.select_item] = self.quantity

            self.item_flag = input("\n" "Do you wish to continue?(Y/N)")
            if self.item_flag == "N":
                break
            
        print("\n" "Please confirm the order given:")
        print(self.order)
        print("\n" "THANK YOU! Please wait while we get your items")
        time.sleep(2)
        print("\n" "Here you go, Please have your order")
        time.sleep(2)

    def billGeneration(self):
        """ Generates bill for the ordered items """
        
        print("\n" "Generating Bill....")
        time.sleep(2)
        print("------------------------------------------")
        current_time = datetime.datetime.now()
        print("Invoice Generated On:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
        print("------------------------------------------")

        for key in self.menu.keys():

           if key in self.order:
              print(key, "\t", "Qty", self.order[key], "\t", "Rs", self.menu[key] * self.order[key])
              self.cost_item = self.menu[key] * self.order[key]
              self.total += self.cost_item

        self.taxamt = lambda amt, tax : amt * tax
        print("------------------------------------------")
        print("TOTAL:", "\t", "\t", "Rs", self.total)
        print("GST 4%", "\t", "\t", "Rs", self.taxamt(self.total, self.tax))
        print("------------------------------------------")
        self.total += self.taxamt(self.total, self.tax)
        print("GRAND TOTAL:", "\t", "Rs", self.total)
        print("------------------------------------------")
        

    def rateService(self):
        """ Display customer ratings of the services provided """
        
        print("\n" "Dear customer, Please Rate our Service * * * * * ")
        rating = input("\n" "Please key-in the Stars : ")
        rating = rating.replace(" ","")
        
        if rating == "*":
            print("Service Rated is:", rating, " TERRIBLE")
        elif rating == "**":
            print("Service Rated is:", rating, " BAD")
        elif rating == "***":
            print("Service Rated is:", rating, " OK")
        elif rating == "****":
            print("Service Rated is:", rating, " GOOD")
        elif rating == "*****":
            print("Service Rated is:", rating, " EXCELLENT")

        
        print("\n" "THANK YOU! PLEASE VISIT AGAIN....")
        
        
#Main Program  
res = Restaurant()

res.menuDisplay()
res.orderConfirm()
res.billGeneration()
res.rateService()
