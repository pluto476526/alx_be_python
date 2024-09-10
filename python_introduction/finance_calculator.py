# This script calculates users' monthly savings and projected savings after one year with interest

# Getting user input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected savings after one year, with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display results
print(f"Your monthly savings are: {monthly_savings}.")
print(f"Projected savings after one year with 5% interest: {projected_savings}.")
