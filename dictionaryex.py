id=int(input("Please enter your id: "))
name=input("Please enter your name: ")
address=input("Please enter your address: ")
contact=input("Please enter your contact no: ")

qualification_name1=input("Please enter your qualification name: ")
passing_year1=input("Please enter your year: ")

qualification_name2=input("Please enter your qualification name: ")
passing_year2=input("Please enter your year: ")

studentdata={
    "id":id,
    "name":name,
    "address":address,
    "contact":contact,
    "qualification": [
        {"qualification_name1":qualification_name1,
        "passing_year1":passing_year1},
        {"qualification_name2":qualification_name2,
         "passing_year2":passing_year2}
    ]   
}
print(studentdata)