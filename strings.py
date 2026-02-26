str1="this is \"a test\""
print(str1)

str2="Elephant"

ex1=str2[0]
print(ex1)

ex2=str2[3:8]
print(ex2)

ex3= str2[:5]
print(ex3)

ex4= str2[5:]
print(ex4)

ex5="james bond"[2:5]
print(ex5)

print("james bond"[2:9])

stra = 'hello'
strb= 'world'
print(stra+strb)
print(stra,strb)
print (len(stra))
length2= len(strb)
print(length2)
print(stra+"\n"+strb)

# INdexing
nameA='Rahul Pravalika'
print(nameA[4])
#Slicing

nameB='This is a test string'
print(nameB[4:6])
print(nameB[4:7])
print(nameB[4:8])
print(nameB[4:8])

#testing different slicing
print(nameB[4:])
print(nameB[4:8])
# negative slicing
print(nameB[-7:-1])
print(nameB[-7:])

str2="i am studying with apna college"
testa=str2.endswith("llege")
print(testa)
testb= str2.capitalize()
print(testb)

# replace function

str3= str2.replace("a",'o')
print(str3)
print(str2.replace("studying","learning"))
print(str2)

# find  funtion
print(str2.find("o"))

print(str2.find("Z"))

#Count function
print(str2.count("a"))

print()
strbname =input("enter you name")
print(len(strbname))



asd="i am the $ orccurances in the $ string"
print()
print(asd.count("$"))


age1=24

if(age1>=18):
    print("Can vote")
elif(age1<18):
    print("cannot vote")
else:
    print("age doesnt exits")

print("code ends here")

age2=24

if(age2>=18):
        if(age2>=60):
             print("cannot drive")
        else:
             print("Can have driving license")
elif(age2<18):
     print( "Cannot drive")
else:
     print("dont know  what to do")


numb1 =int(input("enter a number"))
result =numb1%2
if(result==0):
     print("number is even")
else:
     print("number is odd")


numba=int(input("enter num 1"))
numbb=int(input("enter num 2"))
numbc=int(input("enter num 3"))

if(numba>numbb and numba>numbb):
    print("numb1 is largest")
elif(numbb>numba and numbb>numbc):
     print("numb2 is largest")
else:
     print("numb3 is largest")
     