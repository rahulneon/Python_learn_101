# indexes
from typing import List

lim = ["Hamstrings","test","breakfast","get out of here"]

lim2=lim

tes=lim2[3]+"  "+lim[1]

print(tes)

# indx reassignment

reasg=[2,2,5,6.6,4,3]

reasg[1]=6
print(reasg)


#append value

reasg.append(999)

print(reasg)

# slicing

reasg1=reasg[:3]

print(reasg1)

reasg2=reasg[3:6]
print(reasg2)

reasg3=reasg[3:]
print(reasg3)

#Indexing

value1=reasg.index(3)

print(value1)

strcheck =["These are ","the prick","deal with them"]

strcheck.insert(2,"pricks in life")

print(strcheck)
strcheck.append("don't quit")

print(strcheck)

strcheck.remove("These are ")
print(strcheck)
strcheck.insert(0,"They are")
print(strcheck)

strcheck.remove("the prick")

print(strcheck)


#pop fuction

strcheck1=strcheck.pop(2)

print(strcheck1)

print(strcheck)

strcheck2=strcheck.pop()

print(strcheck2)

print(strcheck)