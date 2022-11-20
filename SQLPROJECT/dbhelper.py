import mysql.connector
class DBhelper:
  def __init__(self):
    self.mydb= mysql.connector.connect(
      host="localhost",
      port="3306",
      user="root",
      password="root123",
      database="prithvi")


    query='create table if not exists bus(id int primary key, state char(20), bus int, citizen_id int, phone_no int)'
    cur=self.mydb.cursor()
    cur.execute(query)
    
    query='create table if not exists travelCard(CitizenId int primary key, Mode char(20), Traveltime varchar(20))'
    cur=self.mydb.cursor()
    cur.execute(query)

    query='create table if not exists user(UserId int primary key, userName varchar(200), phone varchar(12))'
    cur=self.mydb.cursor()
    cur.execute(query)
    print("Created")

#Insert in Train Registration
  def insert_Train(self,citizenid,state,phone):
    query="insert into trainstations(citizen_id,station,phone_no) values({},'{}','{}')".format(citizenid,state,phone)
    # print(query)
    cur=self.mydb.cursor()
    cur.execute(query)
    self.mydb.commit()
    print("Train Registration saved to DB")
  
#Insert in Bus Registration
  def insert_Bus(self,citizenid,state,phone):
    query="insert into bus(citizen_id,state,phone_no) values({},'{}','{}')".format(citizenid,state,phone)
    # print(query)
    cur=self.mydb.cursor()
    cur.execute(query)
    self.mydb.commit()
    print("Bus Registration saved to DB")

#Inser in Travel booking

  def insert_Card(self,citizenid,mode,time):
    query="insert into travelCard(CitizenId,Mode,Traveltime) values({},'{}','{}')".format(citizenid,mode,time)
    # print(query)
    cur=self.mydb.cursor()
    cur.execute(query)
    self.mydb.commit()
    print("travel card saved to DB")

  #Insert in user

  def insert_user(self,userid,username,phone):
    query="insert into user(userId,userName,phone) values({},'{}','{}')".format(userid,username,phone)
    # print(query)
    cur=self.mydb.cursor()
    cur.execute(query)
    self.mydb.commit()  
    print("user saved to DB")

#Fetch_all_TravelStations
  def Trainfetch(self):
    query="select distinct station from trainstations"
    cur=self.mydb.cursor()
    cur.execute(query)
    for row in cur:
      return row

#Fetch_all_self

  def fetch_all(self):    
    query="select * from user"
    cur=self.mydb.cursor()
    cur.execute(query)
    for row in cur:
      print("User Id :    ", row[0])
      print("User Name :  ", row[1])
      print("User Phone : ", row[2])
      print()
      
# Fetch one
  def fetch_one(self,userid):
    query="select * from user where UserId={}".format(userid)
    cur=self.mydb.cursor()
    cur.execute(query)
    for row in cur:
      print(row)
  

# Delete user
  def delete_user(self,userid):
    query="delete from user where userid = {}".format(userid)
    cur=self.mydb.cursor()
    cur.execute(query)
    self.mydb.commit()
    print("deleted")
    print(query)

# Update user

  def update_user(self,userid,newname,newphone):
    query="update user set username = '{}', phone = '{}' where userid = {}".format(newname,newphone,userid)
    print(query)
    cur=self.mydb.cursor()
    cur.execute(query)
    self.mydb.commit()
    print("Updated")
 