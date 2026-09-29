# 2.1: Finding Highest & Lowest Test Scores BEGINNER
# Lists For Loops You have a list of marks obtained by students in a quiz. Find statistics manually using loops.
# marks = [45, 78, 92, 34, 88, 67, 95, 52]
# Use a for loop to find the highest score and lowest score in the list (without using max() or min()).
# Calculate the total sum of all marks using a loop and find the class average score.
# Print the highest score, lowest score, and average mark

marks = [45, 78, 92, 34, 88, 67, 95, 52]

highest_score = marks[0]
lowest_score = marks[0]
total_sum = 0

for mark in marks:
    if mark > highest_score:
        highest_score = mark
    if mark < lowest_score:
        lowest_score = mark
    total_sum += mark

average_score = total_sum / len(marks)

print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Average Mark: {average_score}")