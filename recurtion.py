def power(a,b):
    if b==0:
        return 1
    else:
        return a* power(a,b-1)
#__main__

s=int(input("Enter a number: "))
p=int(input("enter its power: "))

result=power(s,p)
print("the power of ",s," raised to", p," is", result)