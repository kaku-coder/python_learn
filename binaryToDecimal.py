
binary = int(input("give binary Number : "))

decemal = 0
Counter = 0

while binary>0:
    bit = binary%10
    decemal = decemal + bit*pow(2,Counter)
    Counter = Counter+1
    binary = binary//10

print(decemal)