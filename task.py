student={}

student['id']=int(input("Enter Student ID: "))
student['name']=input("Enter Student Name: ")
student['address']=input("Enter Student Address: ")

hindi=int(input("Enter Hindi Marks: "))
english=int(input("Enter Englis Marks: "))
maths=int(input("Enter Maths Marks: "))
science=int(input("Enter Science Marks: "))

total=hindi+english+maths+science

student['percentage']=(total/400)*100

print(student)