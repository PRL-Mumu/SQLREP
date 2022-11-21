from dbhelper import DBhelper

def main():
    db=DBhelper()
    while True:
        print("************WELCOME************")
        print()
        print("Press 1 to insert new user")
        print("Press 2 to display all user")
        print("Press 3 to delete user")
        print("Press 4 to update user")
        print("Press 5 to exit program")
        print()
        print("*******************************")
        print(":>",end=" ")
        try:
            choice=int(input())
            if(choice == 1):
                uid=int(input("Enter user ID: "))
                username=input("Enter user name: ")
                phn=input("Enter phone number: ")
                db.insert_user(uid,username,phn)
                pass
            elif(choice == 2):
                db.fetch_all()
                pass
            elif(choice == 3):
                userid=int(input("Enter userid of which you want to delete: "))
                db.delete_user(userid)
                pass
            elif(choice == 4):
                uid=int(input("Enter Id of user: "))
                username=input("Enter new user name: ")
                phn=input("Enter new phone number: ")
                db.update_user(uid,username,phn)
                pass
            elif(choice == 5):
                break
            else:
                print("Invalid Input ! Try again!")
        except Exception as e:
            print(e)
            print("Invalid Details ! Try again.")
if __name__ == "__main__":
    main()