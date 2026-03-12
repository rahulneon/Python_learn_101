# class student:
  
#     #  #default constructors
#     def __init__(self):
#           pass
    
#     college_name ="SRM"# class attribute
#     name = "anonymous"

#      #Parameterised constructors
#     def __init__(self,fullName,marks):
#         self.name =fullName   # here since object  attribute has higher precedence over class attributes
#         self.marks =marks    
#         print("adding a new student in db")
    
#     def testMtd(self):   # methods are functions that belong to objects
#          print("hello, welcome student",self.name)
    
#     def marksMtd(self):
#          return(self.marks)



# print(student.college_name)

# student1= student("Avinash",90)
# print(student1.name) # due to obj.attr> class.attr  name gets printed
# print(student1)

# s2= student("Rahul K",99)
# print(s2.name,s2.marks)

# print(s2.testMtd())
# print("your percentile is",s2.marksMtd())



# # class Cars:
# #     brand="Porche"
# #     modelName="911"
# #     seaterType="2 seater"
# #     color="blue"

# # car1 = Cars()
# # print(car1.brand)



# class Student:
#     def __init__(self):
#         pass

#     def StudentInfo(self,name,marks):
#         self.name =name
#         self.marks=marks
    
#     def avg(self):
#         sum =0
#         for val in self.marks:
#             sum +=val
#         print("hi ",self.name," your avarage score is: ",sum/3)   
   
#     @staticmethod    #this is a decorator allow us to wrap another function in order to extend the behaviou of the wrapped funtion without permanently modifying it
#     def hello():
#         print("hello this is a static method declaration")

# sData =Student()
# sData.StudentInfo("RahulK",[10,9,8])
# sData.avg()

# sData.name="Bhuvan K"
# sData.avg()

# sData.hello()

class Account():
    def __init__(self,accNo,accName,accBal):
        self.accNo = accNo
        self.accName = accName
        self.accBal = accBal
    
    def deposit(self,amount):
        self.accBal += amount
        print("your new balance is: ",self.accBal)
    
    def withdraw(self,amount):
        if amount > self.accBal:
            print("insufficient balance")
        else:
            self.accBal -= amount
            print("your new balance is: ",self.accBal)
    
    def checkBalance(self):
        return self.accBal

print("welcome to the bank")
acc1 = Account(12345,"Rahul K",10000)
print("your account number is: ",acc1.accNo)
print("your account name is: ",acc1.accName)
print("your account balance is: ",acc1.accBal)  
acc2 = Account(67890,"Bhuvan K",50000)
print("your account number is: ",acc2.accNo)
print("your account name is: ",acc2.accName)
print("your account balance is: ",acc2.accBal)  
acc1.deposit(5000)
acc1.withdraw(2000)
print("your current balance is: ",acc1.accBal)
acc1.withdraw(15000)
print("your current balance is: ",acc1.checkBalance())