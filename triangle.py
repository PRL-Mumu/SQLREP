def triangle_area():
    x=int(input("what is the height of the triangle: "))
    y=int(input("what is the width of the triangle: "))
    sum= x+y
    area= sum/2
    print("the trianglearea is ", area)
    return 0

#__Main__

i=0
while i==0: 
    triangle_area()
    query=input("do you want to calculate again. y/n ")
    if query=="n":
        i=1
    elif query=="y":
        i=0


