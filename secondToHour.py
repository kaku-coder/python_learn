# Write a program to enter seconds from the user and convert them into Hours, Minutes, and
# remaining Seconds using floor division ( // ) and modulus ( % ) operators.

second = int(input("Enter seconds : "))

minite = second // 60
rem_sec = second % 60

hour = minite // 60
rem_min = minite % 60

print(f"Hours : {hour} , Minutes : {rem_min} , Seconds : {rem_sec}", )