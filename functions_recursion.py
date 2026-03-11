# 00:01 Functions in Python are blocks of code that can be reused.
# 02:02 Functions reduce redundant code and improve reusability.
# 06:12 Understanding function calls and parameters in Python.
# 08:09 Using functions reduces redundancy and makes code more efficient.
# 12:13 Functions in Python can be created with or without parameters and return values.
# 14:17 Functions offer a way to encapsulate code for reuse.
# 18:06 Understanding built-in and user-defined functions in Python.
# 19:58 Understanding default parameter values in Python functions
# 24:04 Creating functions to print lists with proper formatting
# 26:09 Understanding functions and recursion in Python
# 30:35 Introduction to functions and recursion in Python
# 32:36 Recursion in Python
# 36:10 Recursion is used to print numbers in a function call
# 37:55 Explaining recursion in Python with a specific example
# 41:39 Understanding the call stack in Python.
# 43:29 Recursion creates layers of function calls
# 46:59 Understanding the concept of recursion and factorial in Python.
# 49:04 Understanding recursion and its application in programming
# 52:51 Understanding recursion through the factorial function
# 54:40 Understanding recursion and writing recursive functions in Python.
# 58:29 Understanding recursion in Python
# 1:00:41 Understanding recursion in Python

sum= 0
def calc_addition(a,b):
    sum =a+b
    print(sum)
    return sum


a= int(input("enter a value for a "))
b= int(input("enter a value for b "))

c = calc_addition(a,b)

print("return function test ",c)


def calc_Mul(a,b):
    return a*b

print(calc_Mul(1,2))

avg_calc_value =0.0

def calc_avg(a,b,c):
    avg_calc_value=(a+b+c)/3
    print(avg_calc_value)

a= int(input("enter a value for avg of a "))
b= int(input("enter a value for avg of b "))
c= int(input("enter a value for avg of c "))

output= calc_avg(a,b,c)

print(calc_avg(a,b,c)) # this gives None as the function has nno return value


print(output)# this gives None as the function has nno return value

print("Rahul K", end=" ")
print("Rahul K","learner")


check_list=["a","b","c","d"]
heroes =["batman","flash"]

def check_len(list):
    print(len(list))


check_len(check_list)
check_len(heroes)

#WAF to print the elements of a list in a single line (list in parameter)

check_list=["a","b","c","d"]
heroes =["batman","flash","superman","wonder woman"]

def check_len(list):
    for val in list:
          print(val, end=" ")
    print(len(list))


check_len(check_list)
check_len(heroes)


#WAF factorial (list in parameter)

num_n= int(input("enter the number to find the factorial "))

def fact(num_n):
     fact =1
     for i in range(1,num_n+1):
         fact *=i
     print(fact)
     
fact(num_n)

# WAF USD To INR

usdVal =float(input("enter the usd currency to convert to inr"))

def curr_conversion(usdVal):
     print("INR value of the entered usd is",usdVal*83)

curr_conversion(usdVal)

#recursions basically  call stack 

def show(n):
    if(n==1): # base case  to stop the recursion
         print(n)
         return
    print(n)
    show(n-1)

show(5)

#Recusrions using factorial

def fact(n):
     if(n==0 or n==1):
          return 1
     else:
          return n* fact(n-1)
     
print(fact(5))   

def SumNnumb(n):
    if(n==1):
        return 1
    else:
        return SumNnumb(n-1)+n

print(SumNnumb(5))


heroes =["batman","flash","superman","wonder woman"]
    
def SumNnumb(list,indx=0):
    if(indx==len(list)):
        return
    print(list[indx])
    SumNnumb(list,indx+1)

SumNnumb(heroes)