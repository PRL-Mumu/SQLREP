from dbhelper import DBhelper

def main():
    db=DBhelper()
    while True:
        print("************WELCOME************")
        print()
        print("Press 1 to register train ticket")
        print("Press 2 to display registered stations")
        print("Press 3 to exit program")
        print()
        
        try:
            choice=int(input())
            if choice==1:
                print("Please enter your details below.")
                State=input("Select State/Locality of Boarding station: ")
                Citizenid=int(input("Enter your Citizen Id: "))
                Phone_No=int(input("Enter your phone number:"))
                db.insert_Train(Citizenid,State,Phone_No)
                pass
            elif choice==2:
                Regstation=db.Trainfetch()
                print("The registered Stations are: \n", Regstation)
                pass
            elif choice==3:
                break
            else:
                print("Invalid input")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()