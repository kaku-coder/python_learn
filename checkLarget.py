# using built in method 


count = 3
array = []

for i in range(count):
    array.append(int(input("Enter Number : ")))

largest = max(array)
print("The largest number is:", largest)


# manual method is

input1 = int(input("Enter first Number ; "))
input2 = int(input("Enter second Number ; "))
input3 = int(input("Enter third Number ; "))

if (input1>input2) & (input1>input3):
    print(f"{input1} is greater then {input2},{input3} two number ")
elif (input2>input1) & (input2>input3):
    print(f"{input2} is greater then {input1},{input3} two number ")
else:
    print(f"{input3} is greater then {input1},{input2} two number ")





