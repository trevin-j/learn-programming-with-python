# Format:

# Please enter your name: Billy
# Hello, Billy !
# Please enter the following information.
# --------------------------------
# Birthday: 5/22/2000
# Favorite ice cream flavor: mint
# Phone number: 123-456-7890
# Address: 123 Address Rd.
# ================================
# Name     Birthday       Favorite Ice Cream    Phone Number   Address
# --------------------------------------------------------------------
# Billy   5/22/2000   mint   123-456-7890   123 Address Rd.



# Get the user's name
user_name = input("Please enter your name: ")
print("Hello,", user_name, "!")

# Get the user's information
print("Please enter the following information.")
print("--------------------------------")
birthday = input("Birthday: ")
ice_cream = input("Favorite ice cream flavor: ")
phone_number = input("Phone number: ")
address = input("Address: ")

# Display the user's information in a table
print("===============================")
print("Name     Birthday       Favorite Ice Cream    Phone Number   Address")
print("--------------------------------------------------------------------")
print(user_name, "   ", birthday, "   ", ice_cream, "   ", phone_number, "   ", address)