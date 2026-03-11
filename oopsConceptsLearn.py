class student:
     
    #  #default constructors
    def __init__(self):
          pass
    
    college_name ="SRM"# class attribute
    name = "anonymous"

     #Parameterised constructors
    def __init__(self,fullName,marks):
        self.name =fullName   # here since object  attribute has higher precedence over class attributes
        self.marks =marks    
        print("adding a new student in db")
    
    def testMtd(self):   # methods are functions that belong to objects
         print("hello, welcome student",self.name)
    
    def marksMtd(self):
         return(self.marks)



print(student.college_name)

student1= student("Avinash",90)
print(student1.name) # due to obj.attr> class.attr  name gets printed
print(student1)

s2= student("Rahul K",99)
print(s2.name,s2.marks)

print(s2.testMtd())
print("your percentile is",s2.marksMtd())



# class Cars:
#     brand="Porche"
#     modelName="911"
#     seaterType="2 seater"
#     color="blue"

# car1 = Cars()
# print(car1.brand)

