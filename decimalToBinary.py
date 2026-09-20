num = int(input("give decimal Number : "))
ans= 0
# while num>0:
#     bit = num%2
#     ans = bit+ans
#     num = num // 2
    
# print(ans)


# second way is inbuild function in pythong 

binary = bin(num)
print(binary[2:]) #string slicing

octa= oct(num)
print(octa[2:])

hexa = hex(num)
print(hexa[2:])