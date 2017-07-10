
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
	r = rate
	n = total_payments

	pmt = r * p / (1 - (1 + r))


def interest_size(remaining_balance, payment, rate):
	pass


def principal_paydown(remaining_balance, payment, rate):
	pass


def recalc_principal(remaining_balance, payment):
	pass

def recalc_cum_prin():
	pass

def recalc_cum_int():
	pass

def recalc_cum_pmt():
	pass