# Write a Python program that counts the number of vowels in a given string using a for loop and an if statement.

vowel = ["a","e","i","o","u"]

sentence = str(input("entery any sentence : "))
vowel_count = 0
for i in range(len(sentence)):
   if sentence[i].lower() in vowel:
    vowel_count+=1

print(vowel_count)