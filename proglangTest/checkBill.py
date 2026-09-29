# Problem 1.1: Store Checkout Bill Calculator BEGINNER
# Operators If / Else Calculate the total bill for a customer buying items at a supermarket.
# item_price = 45.0 quantity = 4 has_membership = True
# Calculate total_cost = item_price * quantity.
# If total_cost is greater than 100 AND has_membership is True, give a $15 discount. Otherwise, give a $5
# discount.
# Print the final bill amount.


item_price = 45.0
quantity = 4
has_membership = True

# Calculate total cost
total_cost = item_price * quantity

# If total_cost >= 100 and has_membership is True, give $15 discount, else $5 discount
if total_cost >= 100 and has_membership:
    discount_amount = 15
else:
    discount_amount = 5

print(f"Discount: ${discount_amount}")

# Calculate and print final bill
final_bill = total_cost - discount_amount
print(f"Final Bill Amount: ${final_bill}")

