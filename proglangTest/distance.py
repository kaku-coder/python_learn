#  Simple Distance & Fuel Expense Function BEGINNER
# Functions Return Values Write a user-defined function to compute travel fuel cost.
# def calculate_fuel_cost(distance_km, fuel_price_per_liter=1.5): # Write your
# code here pass
# Assume a car gives a mileage of 15 km per liter (1 liter per 15 km).
# Calculate total liters needed for distance_km and multiply by fuel_price_per_liter.
# Return the total cost. Test your function with distance_km = 150.

def calculate_fuel_cost(distance_km, fuel_price_per_liter=1.5):
        mileage_per_liter = 15
        total_liters_needed = distance_km / mileage_per_liter
        total_fuel_cost = total_liters_needed * fuel_price_per_liter
        return total_fuel_cost

print(calculate_fuel_cost(150))