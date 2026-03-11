# whileloops
aStr="hello"
# count =1
# while(count<=5):
#         print(aStr)
#         count+=1

# print(count)

newname="Rahul"
# i=1
# while(i<=5000):
#     print(newname)
#     i+=1


i=5
while(i>=1):
    print(aStr)
    i-=1

print("loop Ended")

num=1
while(num<=100):
    print(num)
    num+=1

print("P1 ended")

num=100
while(num>=1):
    print(num)
    num-=1
print("P2 Ended")

mulNum =10
count=0
while(mulNum>=count):
    print(mulNum,"x",count,"=",mulNum*count)
    count+=1

print("multiplicationtable enede")



count=0
while(count<=10):
    print(count,"x",count,"=",count*count)
    count+=1

print("sqr ende")


listA=[1,4,9,16,25,36,49,64,81,100]
count=0
print(len(listA))
while(len(listA)>count):
    print(listA[count])
    count+=1

print("list program ended")

numSearch =(1,4,9,16,25,36,49,64,81,100)
print(type(numSearch))
s= int(input("enter a number to search from the tuple"))
count=0
while(len(numSearch)>count):
    
    if(s==numSearch[count]):
        print("num found at index",count)
        break
    else:
        a="not found" 
    count+=1

print(a,"tuple program ended")

print("testing continue")

count=0
while(count<=10):    
    if(count%2==0):
        count +=1
        continue
    print(count)
    count+=1


list=[1,2,3,4]

for num in list:
    print(num)


list =["potato","Tomato","cucumber","eggplant"]

for veg in list:
    print(veg)


str ="This is my understadnding"

for ch in str:
    print(ch)
    if(ch=="e"):
        break
    else:
         print("end")

print("this is a temp program")

listA=[1,4,9,16,25,36,49,64,81,100]

print(len(listA))
for ele in listA:
    print(ele)
    count+=1

print("list with for program ended")

numSearch =(1,4,9,16,25,36,49,64,81,100)
print(type(numSearch))
s= int(input("enter a number to search from the tuple"))
count =0
for ele in numSearch:    
    if(s==ele):
        print("num found at index",count)
        break
    else:
        a="not found" 
count +=1

#Range funtions are in learning

seq=range(5)
print(range(5))

for sequence in seq:
    print(sequence)


for seq in range(1,25,2):  # range(start,stop,step size)
    print(seq)


for num in range(1,100,2):
    print(num)


for num in range(1,100,1):
    print(num)

for num in range(100,1,-1):
    print(num)


# pass is used for  fututre code used in exceptions and try caatch



# Practice  questions  WAP to find the sim of first n numbers using while

#WAPto find the factorial of first n numbers( using for)






