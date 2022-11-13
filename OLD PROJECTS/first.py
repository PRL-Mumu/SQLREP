'''
#TRAVEL BOOKING

x=int(input("Enter citizen id:"))
y=int(input("Enter time of travel 1-24 :"))
z=input("Enter mode of transport ( bus / train ) :")
print("\nBooking Ecard for transport")
print("\ncitizen id:",x,"\ntravel time",y,"\nTransport mode",z)
print("\n Ecard succesfully booked")
'''
'''
#HIMANSHU RETAILERS

print("Welcome to Himanshu Retailers.")

x=input("Enter 'y' to begin billing: ")

if x=='y':
    print("Enter your details")
    y=input("Enter item name:")
    z=int(input("Enter item id:"))
    p=int(input("Enter citizen id:"))
    q=int(input("Enter item price:"))

elif x!='y':
    print("Billing canceled!")
    exit()

print("Printing BILL")
print("___________________________________")
print("|                                  |")
print("|                Bill              |")
print("|__________________________________|")

print("ITEM:-",z)
print("Provider id-",p)
print("Price:",q)
'''



#SHOPPING LIST

t=["cake", "vegetables", "coffee","apples"]
print("Shopping list")
print(t)
a=input("Do you want to add an item to the list (Y/N)")
if a=="Y":
    b=input("Enter the item name: ")
    t.append(b)
    print("The new shopping list is:- ",t,"\n")
elif a=="N":
    print("List not updated...")
else:
    print("Input Error!!")

