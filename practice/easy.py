# 1. Take a number as input and check whether it is positive, negative, or zero.


# if input > 0:
#     print("this is positive")
# elif input == 0 :
#     print("this is zero")
# else :
#     print("this is negative")




#2. Take a number and check whether it is even or odd.

# if input%2 == 0:
#     print("this is even number ")
# else:
#     print("this is odd number ")

# Find the largest of three numbers.

# store_arry = []

# for i in range(3):
#     num = int(input("Enter a number : "))
#     store_arry.append(num)

# print(max(store_arry))

# 4. Print all numbers from 1 to N.

# n = int(input("Enter the Number : "))
# for i in range(n):
#     print(i+1)


# 5. Print the multiplication table of a given number.

# table = int(input("Enter Table Number : "))

# for i in range(1,11):
#     print(f"{table}*{i}={table*i}")



#  6. Find the sum of numbers from 1 to N.

# sum = 0;
# num = int(input("Enter the Number : "))

# for i in range(num+1):
#     sum +=i
# print(sum)

#7. Count the number of vowels in a string.

# vowel = 'a,e,i,o,u'
# string = str(input("enter any word : "))
# count = 0
# lowercase = string.lower()
# print(lowercase)
# for char in lowercase:
#     if char in vowel:
#         count+=1

# print(count)


# 8. Reverse a string without using [::-1]


# charactor = "hello world"
# revese_text ="".join(reversed(charactor)) 
# print(revese_text)


#9. Find the largest element in a list without using max().

# list_element = [1,2,3,4,5,65,67]
# start_index = list_element[0]

# for i in range(len(list_element)):
#     if list_element[i]>=start_index:
#         start_index=list_element[i]

# print(start_index)


#10. Remove duplicate elements from a list while maintaining the original order.

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numebr = list(set(numbers))
print(unique_numebr)