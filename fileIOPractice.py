with open("praactice.txt","w")as f:
    f.write("hi everyone \n we are learning file i/o \n")
    f.write("implementing in java\n i love  coding in java")

with open("praactice.txt","r") as f:
    data=f.read()

new_data =data.replace("java","python")
print(data)
print(new_data)

with open("praactice.txt","w") as f:
    f.write(new_data)

print(data)
def checkForWord(word):
        with open("praactice.txt","r") as f:
          data=f.read()
        if(data.find(word)!=-1):
            print("found")
        else:
         print("notfound")

word =input("enter the work you are searching for")
checkForWord(word)


def checkForWord(word):
        with open("praactice.txt","r") as f:
          readData= True
          lineno=1
          while(readData):
                readData=f.readline()
                if(word in readData):
                    print("found",lineno)
                    return # if  we remove this  it will reach till the end of the entire text in the practice file
                else:
                    print("-1")
                lineno+=1

word =input("enter the work you are searching for : ")
checkForWord(word)


numberData="1,2,3,4,5,32,21,5,4,2,8,0,6,8,354,353"

# with open("praactice.txt","w")as f:
#     f.write(numberData)

newnumberData =""

with open("praactice.txt","r") as fileData:
    newnumberData = fileData.read()

print(newnumberData)

# currNum =""
# for i in range(len(newnumberData)):
#     if(newnumberData[i]==","):
#         print(int(currNum), "")
#         currNum=""
#     else:
#         currNum+=newnumberData[i]

count =0

num= newnumberData.split(",")
for val in num:
    if(int(val)%2!=0):
        count+=1
        
print(count)

