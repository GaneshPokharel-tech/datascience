from finance_tools.tax import calculate_tax
from finance_tools.loan import calculate_emi


def get_float_input(Enter your monthly salary (NPR): ):
    while True:
        try:
            value = float(input(Enter your monthly salary (NPR):))
            return value
        except ValueError:
            print("Invalid input Please enter a numeric value.")

'''tax calculation'''
income = get_float_input("Enter your annual income: ")
tax_amount = calculate_tax(income)
print(f"Your tax amount is: {tax_amount}")
print("-" * 30)

'''emi calculation'''
principal = get_float_input("Enter loan amount: ")
rate = get_float_input("Enter annual interest rate (%): ")
time = get_float_input("Enter loan duration in years: ")

emi = calculate_emi(principal, rate, time)
print(f"Your monthly EMI is: {emi}")

