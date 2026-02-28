marks =[94.4,87.5,54.4,43.3,75.4,98]
print (marks )
print(type(marks))
print(marks[1])
print(len(marks))
student =["Rahul","Bhuvan","Pravalika"]
print(student)

#Lists are mutable as strings are not  mutable  in list  indexes can be  changed

student[0]="Rahul K"
print(student)

#List slicing

print(student[1:])
print(student[-3:-1])
print(student[-2:])

# List methods
list =[2,1,3]
list.append(4)
print(list)
#sorting a list
print(list.sort()) #this  returns none as it only changes internally and doesnt  prints data
print(list)

print(list.sort(reverse=True))
print(list)

list =["a","b","c"]
list.append("d")
print(list)
#sorting a list
list.sort() #this  returns none as it only changes internally and doesnt  prints data
print(list)

list.sort(reverse=True)
print(list)

#list.append("5")
#list.sort() # this  gives an error as the list in build of str and not any int and the sorting gets messy

list =["c","a","b","d"]
list.reverse()
print(list)

list.remove("c")
print(list)

list =[2,1,3,4]

list.insert(2,5)
print(list)

# pop method
list.pop(2)
print(list)

# tuples to create immutable sequence of values
tup =(12,1232,3545,6576,745,4343,43434,466)
print(type(tup))

print(tup[2])

#tup[0]=4
tup=()
print(tup)
print(type(tup))

tup=(1)
print(tup)
print(type(tup))

tup=("a")
print(tup)
print(type(tup))

tup=(1,2,3,4,)
print(tup)
print(type(tup))

#tuple methods
tup=(1,2,3,4,5,3,2,2,1,3,4,3,22,2,2,2)
print(tup.index(2))
print(tup.count(2))

movieList=[]
a =input("enter the name of a movie 1")
movieList.append(a)
b =input("enter the name of a movie 2")
movieList.append(b)
c =input("enter the name of a movie 3")
movieList.append(c)

movilist =[a,b,c]


print(movilist)
print(movieList)

# palindrome check in a list

list=[1,2,3,2,1]

list2= list.copy()
list.reverse()

if(list==list2):
    print("is a palindrome")
else:
    print("not a palindrome")    

gradeTuple =("A","C","B","A","B","A","C","B","B")

print(gradeTuple.count("A"))


gradeTuple.sort()
print(gradeTuple)

