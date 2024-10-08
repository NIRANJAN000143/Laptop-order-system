#TODO: Write the code for the laptop order system.
#TODO: print Welcome message to the customer
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>>> Welcome to the Laptop Order System <<<!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#TODO: Collect customer information
name = str(input("Enter Your Name: "))
number = int(input("Enter Your Phone Number: "))
gmail = input("Enter Your Gmail ID: ")

def laptop_order():
    laptop_view = str(input("Enter the laptop brand you want to order (e.g., Asus, Lenovo, HP, Dell, Apple): \n"))
    laptop_model_choice = str(input("Enter the model of the laptop you want to order (e.g., 15-inch, 13-inch, 17-inch, 11-inch): "))
    quantity = int(input("Enter the quantity of the Laptop you want to order: "))
    
    #TODO: Call the laptop_model function to validate the selected model
    laptop_model(laptop_model_choice)
    
    #TODO: Get and display the price of the selected laptop brand
    laptop_price(laptop_view, quantity)

def laptop_model(model):
    #TODO: Validate the model input
    if model in ["15-inch", "11-inch", "13-inch", "17-inch"]:
        print(f"You have selected {model} laptop.")
    else:
        print("Invalid input! Please enter a valid model of the laptop you want to order.")

def address_details():
    address = input("Enter your address: ")
    city = input("Enter your city: ")
    state = input("Enter your state: ")
    pincode = int(input("Enter your pincode: "))
    
    #TODO:Print the order summary
    print("\nOrder Summary:")
    print(f"Customer Name: {name}")
    print(f"Phone Number: {number}")
    print(f"Gmail ID: {gmail}")
    print(f"Address: {address}, City: {city}, State: {state}, Pincode: {pincode}")
    
    #TODO: Automatic message after collecting the address
    print("\nThank you! Your order has been placed successfully and will be processed shortly.")

def laptop_price(laptop_model_choice, quantity):  
    # Using the parameter 'laptop_model_choice' passed from laptop_order function 
    price_per_unit = {
        "Asus": 40000,
        "Lenovo": 60000,
        "HP": 45000,
        "Dell": 50000,
        "Apple": 145000
    }.get(laptop_model_choice, None)  # Get price or None if invalid

    if price_per_unit is None:
        print("Incorrect input! Please enter a valid laptop brand!")
        return  # Exit the function if the input is incorrect

    #TODO: Display the price information
    print(f"The price of the selected {laptop_model_choice} laptop is ₹{price_per_unit}.")
    
    # Total price calculation
    total_price = price_per_unit * quantity
    print(f"You have ordered {quantity} laptops. The total price will be ₹{total_price} rupees.")

#TODO: Customer decides to place an order
customer_order_place = input("Do you want to place an order (y/n)? ").strip().lower()
if customer_order_place == "y":
    laptop_order()
    address_details()
else:
    print("Thank you for visiting us!")

#TODO: Ask user if they want to place an online order
customer_online_order = input("Do you want to place an order online (y/n)? ").strip().lower()
if customer_online_order == "y":
    number = int(input("Enter your phone number: "))
    print("Thanks for placing the order online!.")
else:
    print(f"Okay {name}, you can give in hand!")

