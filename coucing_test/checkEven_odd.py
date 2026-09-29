# Write a program that separates even and odd numbers from a list into a dictionary.

array_number = [10, 15, 20, 25, 30]

output = {
    'even': [],
    'odd': []
}

for num in array_number:
    if num % 2 == 0:
        output['even'].append(num)
    else:
        output['odd'].append(num)

print(output)
