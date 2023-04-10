temp_list=[]

fname=input("enter fname")
lname=input("enter lname")

temp_list.append(fname)
temp_list.append(lname)

print(temp_list[0])
print(temp_list[1])

student_rec =[]

student_rec.append(temp_list)

data =[9, 50.55,"muhammed kahn",["muhammed","khan"],{"name":"khan"}]

print(data[3])

sizeofdata = len(temp_list)

print(sizeofdata)
print(len(student_rec))

