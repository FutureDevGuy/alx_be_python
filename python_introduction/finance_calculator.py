# Prompt the user for their monthly income
# Use float() to allow for decimal values in income
monthly_income = float(input("Enter your monthly income: "))

# Ask for their total monthly expenses
# Use float() to allow for decimal values in expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Define the annual interest rate
annual_interest_rate = 0.05 # 5% as a decimal

# Calculate the projected savings after one year
# Formula: Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

# Print the results
print(f"Your monthly savings: ${monthly_savings:.2f}") # .2f for 2 decimal places
print(f"Projected annual savings with interest: ${projected_annual_savings:.2f}")