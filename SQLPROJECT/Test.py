# list1=[1,3,6,93,62]
# max=0
# for i in list1:
#     if i > max:
#         max=i
# print(max)

# a=int(input("Enter the max num: "))
# sum=0
# n=0
# for i in range(0,a):
#         n=n+1
#         sum=sum+n
# print(sum)

# a=int(input("Enter the max number: "))
# b=0
# for i in range(1,a+1):
#         if i%2!=0:
#            b=b+i
# print(b)

# n=int(input("How many students? "))
# compwinners={}
# for i in range(n):
#    key=input("Name of the student:")
#    value = int(input("Number of competition won: "))
#    compwinners[key]=value
# print("the dictionary now is:")
# print(compwinners)

# M={}
# n=int(input("How many students? "))
# for i in range(n):
#         x,y =eval(input("enter roll no, marks: "))
#         M[x]=y
# print(M)

# M={1:90, 2:91, 3:91}
# print("Dictionary: ")
# print(M)
# while True:
#         question=input("do you want to delete another roll no? ")
#         if question.lower()=='yes':
#             xno=int(input("Roll no to be deleted? "))
#             M.pop(xno)
#         else:
#                 break
#         print(M)
        
        # if xno in M:
        #         M.pop(xno)
        #         print(M)

mydict={'x':502,'y':676,'z':100}
keymax=max(mydict.keys(),key=lambda k:mydict[k])
keymin=min(mydict.keys(),key=lambda k:mydict[k])
print('maximum value: ', mydict[keymax])
print('minimum value: ', mydict[keymin])