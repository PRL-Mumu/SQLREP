from dbhelper import DBhelper

def main():
    db=DBhelper()
    while True:
        print("************WELCOME************")
        print()
        print("Press 1 to Book a Cab")
        print("Press 2 to display Scheduled Bookings")
        print("Press 3 to exit program")
        print()
        
        try:
            choice=int(input())
            if choice==1:
                print("\nPlease enter your details below.\n")
                Pickup=input("Enter Pickup Location: ")
                cabdrop=input("Enter drop location: ")
                Citizenid=int(input("Enter your Citizen Id: "))
                size=input("Select size of Cab (2/4) Seater: ")
                db.insert_Cab(Citizenid,Pickup,cabdrop,size)
                pass
            elif choice==2:
                Booking=db.CabFetch()
                print("The Booking details are: \n", Booking)
                pass
            elif choice==3:
                break
            else:
                print("Invalid input")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()