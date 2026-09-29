current_savings = 50
weekly_deposit = 20
target_savings = 200

weeks = 0

while current_savings < target_savings:
    current_savings += weekly_deposit
    weeks += 1

print(f"Target reached in {weeks} weeks! Final savings: ${current_savings}")

