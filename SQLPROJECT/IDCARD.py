from dbhelper import DBhelper

def main():
  db=DBhelper()
  tag="passed"
  while True:
    try:
        tag="passed"
        x = int(input("Enter Citizen Id: "))
        y = int(input("Enter time of travel: "))
        z = input("Enter mode of transport (Bus/Train): ")
        db.insert_Card(x,z,y)
    except Exception as e:
        print(e)
        tag="failed"

    if tag=="passed":   
        print("Booking E-Card for transport.")
        print("CitizenId:",x)
        print("Travel time:",y)
        print("Mode of transport:",z)
        print("E-Card booked succesfully!!")
    elif tag=="failed":
        print("Booking Failed")

    break

if __name__ == "__main__":
    main()
