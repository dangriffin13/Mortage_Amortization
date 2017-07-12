
class MthAmort:
	def __init__(self,
				payment_period, 
				payment,
				principal_payment,
				interest_payment,
				remaining_balance,
				cumulative_principal_payment,
				cumulative_interest_payment,
				cumulative_total_payment
				):
		self.period = payment_period
		self.pmt = payment
		self.prin_pmt = principal_payment
		self.int_pmt = interest_payment
		self.bal = remaining_balance
		self.prin_cum = cumulative_principal_payment
		self.int_cum = cumulative_interest_payment
		self.pmt_cum = cumulative_total_payment


def payment_size(principal, rate, total_payments):
	p = principal
	r = rate/12/100
	n = total_payments

	pmt = r * p / (1 - (1 + r)**-n)
	return pmt


def interest_size(remaining_balance, rate):
	interest = remaining_balance * rate
	return interest

def principal_paydown(remaining_balance, payment, rate):
	paydown = payment - (remaining_balance * rate)


def recalc_principal(remaining_balance, rate):
	principal = remaining_balance - principal_paydown(remaining_balance, payment, rate)

def recalc_cum_prin():
	pass

def recalc_cum_int():
	pass

def recalc_cum_pmt():
	pass