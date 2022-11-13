# make add subtract multiply divide power root factorial

def add():
    print("_________Addition__________")
    a=int(input("Input a number: "))
    b=(input("Input next number: "))

    end=False
    while end==False:
     if  str(b.endswith('end'))==True:
         b=b.strip("end")
         b=int(b)        
         end=True
     else:
        b=(input("Enter next number"))
        if  str(b.endswith('end'))==False:
                c=a+int(b)
                b=b.strip("end")
                b=int(b)
                c=c+b
                
        else:
            c=c+int(b)
    print(c)

add()

print("YEAH THIS IS NOT SO ADVANCED RIGHT NOW.")
    

