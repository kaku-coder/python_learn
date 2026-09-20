# swap two variable enter by the user 

a = int(input("enter a number : "))
b = int(input("enter b number : "))

c=a+b
a=c-a
b=c-b

print("the value of a is",a)
print("the value of b is",b)    



# second way is (using bit manupulation)
a = a ^ b
b = a ^ b
a = a ^ b

print("the value of a is", a)
print("the value of b is", b)


# third way is (using python feature)

a,b = b,a

print("the value of a is",a)
print("the value of b is",b)

# four method is (using division and multiplication)

a = a * b
b = a / b
a = a / b

print("the value of a is",a)
print("the value of b is",b)    


