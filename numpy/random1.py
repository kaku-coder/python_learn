# random number generate


import numpy as np

# random integer generate betweeen 10 and 50

randomInteger = np.random.randint(10,50)
print(randomInteger)


# random decimal value 
randomDecemal = np.random.random()*20
print(randomDecemal)


# suffele the number in array  
number = [1, 2, 3, 4, 5, 6]

np.random.shuffle(number)

print(number)

# random number using rand 

print((np.random.rand(3, 3))*20)