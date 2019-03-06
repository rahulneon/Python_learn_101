tuple1=(5.6,"rhode island",True,1)
tuple2=2,"hero",9.56,False

print(tuple1)
print(tuple2)

empTup=()
print(tuple2)

print(tuple2[2])
print(tuple2[1])

print(tuple2[:3])
print(tuple1[3:])
print(tuple2[1:3])


#For loops

list1=[1,3,6,9]
tuple3=8,6,4,2
for elements in list1:
    print( elements   )


print("abcdefghijklmnopqrstuvwxyz")
for elements in tuple3:
    print(elements)

listy=[4,3,2,1,0]
listy2=[]
for nums in listy:
    listy2.append(nums*4)

print(listy2)


tuplese=("let it be "," i dont care","shit","dark and dead inside","fuck it","dipshit")
#tuplese=(1,5,6,3)
stree=""

for stress in tuplese:
  stree += stress
print(stree)


var1=("Bohr","liebniz","Einsiten")
var2=[]
var3=[9,8,7,6,5,4,3,2,1,0]

var4=[]

for items in var1:
    print(items)

for items in var3[2:8]:
    var2.append(items)

for items in var3:
    if items>1 and items<8:
            var4.append(items)

print(var4)



print(var2)
