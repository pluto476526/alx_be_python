# This script calculates users monthly savings
monthlyIncome = input("Enter your monthly income:")
monthlyIncome = int(monthlyIncome)
monthlyExpenses = input("Enter your total monthly expenses:")
monthlyExpenses = int(monthlyExpenses)

# Calculate monthly savings
monthlySavings = monthlyIncome - monthlyExpenses

projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)

print('Your monthly savings are', monthlySavings, '.')
print('Projected savings after one year, with interest, is:', projectedSavings, '.')
