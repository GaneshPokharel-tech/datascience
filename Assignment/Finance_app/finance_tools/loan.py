def calculate_emi(principle,rate,time):
	total_interest = principle * rate * time
	total_amount = principle + total_interest
	months = 12
	emi = total_amount / 12
	return emi
	