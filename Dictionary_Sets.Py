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
    "subjects":{"
    "physics":98,
    "Maths":43
    }
}