# Weekly Attendance Counter BEGINNER
# For Loops Counting A teacher records daily student attendance over 7 days (1 for present, 0 for absent).
# attendance_record = [1, 1, 0, 1, 1, 0, 1]
# Use a simple for loop to count how many days the student was present.
# Count how many days the student was absent.
# Print a summary: "Present: X days, Absent: Y days"


attendance_record = [1, 1, 0, 1, 1, 0, 1]

present = 0
absent = 0

for day in attendance_record:
    if day == 1:
        present += 1
    else:
        absent += 1

print(f"Present: {present} days, Absent: {absent} days")