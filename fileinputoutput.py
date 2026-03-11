f= open("demo.txt","r+")

data2= f.readline()
data3= f.readline()
data =f.read()
print(data2)
print(data3)
print(type(data))
print(data)
f.close()

f= open("demo.txt","w")

f.write("i want to learn javascript tomorrow then i will move to react JS.")
f.write("i then move on")
f.write("\ni want to learn C#.")

f.close()

f= open("demo.txt","r+")
f.write("This is the learninc  of  file read in python.") # pointer start from  begining and replacing character wise
f.close


f= open("demo.txt","r+")
print(f.read())
 
with open("demo.txt","r") as f:
        data=f.read()
        print(data)

with open("demo.txt","a+") as f:
        f.write("Check yourself before you wreck yourself")
        print(data)