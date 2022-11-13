file1=open("Python program folders\editfile.txt","rb+")
str1="prithviraj is the best"
file1.write(str1)
s = file1.readlines()

print(s)
file1.close()