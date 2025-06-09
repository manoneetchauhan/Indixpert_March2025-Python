num1=int(input("Please Enter Any Number: "))
num2=int(input("Please Enter Any Number: "))

print("Press a for Sum: ")
print("Press b for Subtract: ")
print("Press c for Division: ")
print("Press d for Multiply: ")

num=input("Please select option: ")

if num == 'a':
    print("sum:", num1+num2)
elif num == 'b':
    print("subtract:", num1-num2)
elif num == 'c':
    print("division:", num1/num2)
elif num == 'd':
    print("multiply:", num1*num2)
else:
    print("Error")