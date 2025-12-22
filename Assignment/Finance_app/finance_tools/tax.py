def calculate_tax(income):
	if income <= 500000:
		tax = income * 0.01
	else:
		tax = income * 0.10

	return tax 