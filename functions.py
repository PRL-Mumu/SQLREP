def greet(name):
    print (f"Hi {name}")

def get_greeting(name):
    return f"Hi {name}"

message= get_greeting("Mosh")
file = open("Python program folders\editfile.txt","w")
file.write(message)