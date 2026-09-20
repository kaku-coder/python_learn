# Write a script that reads a character input from the user and displays its corresponding ASCII
# value using ord() , then converts an ASCII integer back to a character using chr() .


charactor = input("Enter a charactor : ")
print("the ascii number is : ",ord(charactor))

num = int(input("enter an ascii number : "))
print("the ascii charactor is : " ,chr(num))