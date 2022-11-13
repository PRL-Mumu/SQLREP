
t=0
ITE2=[]
while True:
  a=input("Enter item name-")
  b=input("Enter item code-")
  c=int(input("Enter price of item-"))
  d=input("Enter the category of item-")
  e=input("Enter the availability of item-")
  ITE1=[a,b,c,d,e]

  x=input("Do you want to add another item?(Y/N): ")
  if x=="y":
    ITE1=[a,b,c,d,e]
    ITE2.append(ITE1)
    t= t+c
    
  elif x=="N": 
    ITE1=[a,b,c,d,e]
    ITE2.append(ITE1)
    t= t+c
    print("                  BILL:\n\n")

    print(":    NAME    :   CODE   :   PRICE   : CATEGORY  :   AVAILABILITY   :")
    
  for item in ITE2:
      print(":", item[0]," "*(9-len(item[0])),":", 
      item[1]," "*(7-len(item[1])),":",
      item[2]," "*(8-len(str(item[2]))),":",
      item[3]," "*(8-len(item[3])),":",
      item[4]," "*(14-len(item[4])),":")
      print("Total is-",t)
      break

    

    