# Create a function count_vowels() that accepts a string and returns the number of vowels.

from numpy._core.defchararray import lower
vowel = "a,e,i,o,u"
word = str(input("give any kind of word or sentence : "))
count = 0
word_lowercase = word.lower()
for text in word_lowercase:
    if text in vowel:
        count+=1

print(count)