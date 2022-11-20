from dbhelper import DBhelper

def main():
    db=DBhelper()
    while True:

        try:
            print("welcome to Public airport registration portal!")
            x=input("Enter 'y' to register a plane ticket: ")

            if x=='y' or x=='Y':
                print("Please enter your details below.")
                State=input("Select State/Locality of Boarding station: ")
                Citizenid=int(input("Enter your Citizen Id: "))
                Phone_No=int(input("Enter your phone number:"))
                db.insert_Plane(Citizenid,State,Phone_No)
            else:
                break
                
        except Exception as e:
            print(e)
if __name__ == "__main__":
    main()