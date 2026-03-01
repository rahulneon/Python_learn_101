infor ={
    "key": "value1",
    "name": "Rahul",
    "learning" :"python"
}
print(infor)

newInfo={
    "College Name" :"Rahullearning center",
    "Language":["c","c++","Java","C#","Python"],
    "studentGender":{"male","Female"},# commonly only tuples care used as key value
    "stuName" :"Bhuvan",
    "Age":"2",
    "course mode":{"online","offline"},
    12:343,# accepts  in as  key value
    12.4:21312
}

print(newInfo)

# disctionary is mutable
print(newInfo["College Name"])
print(newInfo["course mode"])
newInfo["College Name"]=="RK College"
print(newInfo["College Name"])
newInfo["surname"]="Katukury"

print(newInfo)

empty_Dict ={}
print(empty_Dict)
empty_Dict["Name"]="Rahul K"

print(empty_Dict)

studentInfo={
    "Name":"Bhu1",
    "subjects":{
    "physics":98,
    "Maths":43,
    "Social":34,
    "BIology":545
    }
    }
print(studentInfo["subjects"]["Maths"])
print(studentInfo["subjects"]["Social"])

#retuns all the keys
print(studentInfo.keys())

print(len(studentInfo))

listNewStud=list(studentInfo)

print(listNewStud)

#values of dictionary
print(list(studentInfo.values()))

#to get all key values as couple
print(studentInfo.items())

coupleList =list(studentInfo.items())

print(coupleList)


print(studentInfo["Name"])
print(studentInfo.get("Name"))

#print(studentInfo["Names"])  the  key doesnt  exits so this gives and error
print(studentInfo.get("Names")) #  this get method  returns a none helps with large data this is better way to handle the error handling

#Update method
studentInfo.update({"city": "Delhi"})

print(studentInfo)

new_dict={"age":"21"}
studentInfo.update(new_dict)
print(studentInfo)

# Sets in pythons can't store  list and  dict as they are mutable  
#sets are unordered as  the  order of  items in set is not always the same

numbers={1,2,3,4,5}
sets2 ={1,2,2,3,4,4,5,6,7.12,8.21,8.21}
print(numbers)
print(sets2)

collect ={1,2,3,4,4,4,5,"hello","bolo","hello","worlds",6}

print(collect)
print(type(collect))
print(len(collect))
print(collect)

collection =set()
print(collection)
print(type(collection))

# Methods  is sets sets are  mutable  but the elements are immutable

coll =set()
coll.add(1)
coll.add(2)
coll.add(3)
coll.add("chao")
print(coll)
coll.add((1,2,3)) # sets allows int,bool,string,float  and  tuples as they are immutable
print(coll)
#coll.add([3,4,5])# throws an error as list allow mutation un hashable type
coll.remove(2)
print(coll)

print(len(coll))
coll.pop()
print(coll)
coll.add(4)
print(coll)
coll.clear()
print(coll)

#learnign about unuin and intersections

set1={1,2,3}
set2={2,3,4,5}

print(set1)
print(set1.union(set2),"uniion")
print(set2)
print(set1.intersection(set2),"intersection")
print(set1)
print(set2)


#PRactice

dictTable={"table":("a piece of furniture","lists od facts and figures"),"cat": "a small animal"}
print(dictTable)
dictTable2={"table":"a piece of furniture","table":"lists od facts and figures","cat": "a small animal"}
print(dictTable2) # always if same keys are given then the latest is consideered in dictionary
print(type(dictTable))

classroom={"python","c","java","c++","C#","Python","Javascript","java","c++","C#","Python","Javascript"}

print(len(classroom))

subject={"python","c","java","c++","Python"}

dict_User={}

a=input("enter the name of the student")

c=input("enter the subject of the student")

b=int(input("enter the marks of the student"))

dict_User.update({a:[c,b]})
print(dict_User)
print(type(dict_User))

values ={9,9.0}
print(values)
values ={9,"9.0"}
print(values)
values2={("float",9.0),("int",9)}
print(values2)
print(type(values2))

















