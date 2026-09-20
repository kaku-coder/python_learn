name = str(input("Enter Your Name : "))
age = int(input("Enter Your Age : "))
salary = float(input("Enter Your Salary : "))

# print("Name : ", name)
# print("Age : ", age)
# print("Salary : ", salary)

# second way is suing formated string 

print(f"NAME\t\t:\t{name}", 
    f"AGE\t\t:\t{age}", 
    f"SALARY\t\t:\t$ {salary}", 
    sep="\n", 
    end="\n\n"
    )