
import math
#Part 1: Calculating the Circumference 

#Defining the funtion
def print_circum(radius):
    C = 2 * math.pi * radius             #"C" Stands for Circumference 
    print()
    print("The circle's circumference is.", C)

#Calling the funtion to print the circumference with three different values
print_circum(2.3)
print_circum(5)
print_circum(3.5)

    


#Part 2Developing a catalog for my Company 
#Defining The function for the Catalog

def yawa_catalog_drinks(drink_1, drink_1_price, drink_2, drink_2_price, drink_3, drink_3_price):
    combo_1 = drink_1_price + drink_2_price - 10/100 * drink_1_price - 10/100 * drink_2_price
    combo_2 = drink_2_price + drink_3_price - 10/100 * drink_2_price - 10/100 * drink_3_price
    combo_3 = drink_1_price + drink_3_price - 10/100 * drink_1_price - 10/100 *  drink_3_price
    gift_pack = drink_1_price + drink_2_price + drink_3_price - 25/100 * drink_1_price - 25/100 * drink_2_price - 25/100 * drink_3_price 
    
#Printing the Catalog Computations for the Discount 
    print()
    print("Output:")
    print()
    print("Online Store")
    print("------------------------------------------")
    print("Product(s)", "                                                ", "Price")
    print()
    print(drink_1, "                                                      ", "UGX", drink_1_price * 100/100)
    print(drink_2, "                                                     ", "UGX", drink_2_price *100/100)
    print(drink_3, "                                                    ", "UGX", drink_3_price * 100/100)
    print("Combo 1", "(", drink_1, "+" , drink_2, ")", "10% off", "                          ", "UGX", combo_1)
    print("Combo 2", "(", drink_2, "+" , drink_3, ")", "10% off", "                        ", "UGX", combo_2)
    print("Combo 3", "(", drink_1, "+" , drink_3, ")", "10% off", "                         ", "UGX", combo_3)
    print("Gift Pack", "(", drink_1, "+" , drink_2, "+", drink_3, ")", "25% off", "               ", "UGX", gift_pack)
    print()
    print("________________________________")
    print()
    print("For Deliveries Contact: +256757726388")
    print()
    print()

#Calling the Function to Print the catalog
yawa_catalog_drinks("Coke", 1000, "Fanta", 2000, "Sprite", 2500)


