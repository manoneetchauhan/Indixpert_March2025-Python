num1=int(input("Please Enter Any Number: "))
num2=int(input("Please Enter Any Number: "))

print("Press 1 for Sum: ")
print("Press 2 for Subtract: ")
print("Press 3 for Division: ")
print("Press 4 for Multiply: ")

num=int(input("Please select option: "))

if num==1:
    print("sum:", num1+num2)
elif num==2:
    print("subtract:", num1-num2)
elif num==3:
    print("division:", num1/num2)
elif num==4:
    print("multiply:", num1*num2)
else:
    print("Error")