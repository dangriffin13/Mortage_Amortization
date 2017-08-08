
class Mortgage:
	def __init__(self, principal, rate, term):
		self.principal = principal
		self.rate = rate
		self.term = term


class MthAmort:
	def __init__(self, mortgage): #a mortgage object is passed in
		self.bal = mortgage.principal
		self.period = 0
		self.pmt = payment_size(mortgage.principal, mortgage.rate, mortgage.term * 12)
		self.prin_pmt = 0
		self.int_pmt = 0
		self.prin_cum = 0
		self.int_cum = 0
		self.pmt_cum = 0


	def interest_size(remaining_balance, rate):
		interest = remaining_balance * rate
		return interest

	def principal_paydown(remaining_balance, payment, rate):
		paydown = payment - (remaining_balance * rate)	
		return paydown

	def recalc_principal(remaining_balance, rate):
		remaining_balance -= remaining_balance - principal_paydown(remaining_balance, payment, rate)
		return remaining_balance

	def recalc_cum_prin(prin_cum, remaining_balance, payment_period, rate):
		prin_cum += principal_paydown(remaining_balance, payment_period, rate)
		return prin_cum

	def recalc_cum_int(int_cum, remaining_balance, rate):
		int_cum += interest_size(remaining_balance, rate)
		return int_cum

	def recalc_cum_pmt(pmt_cum, principal, rate):
		pmt_cum += principal * rate
		return pmt_cum


def payment_size(principal, rate, total_payments):
	p = principal
	r = rate/12/100
	n = total_payments

	#(1+r)**-n discounts by rate r for n time periods
	#(1 - (1 + r ** -n)) basically tells you how much you need to pay now to
		# make up for the FV - PV diff at the current interest rate.
		# In other words it's the present value of an interest payment
		# you divide the principal by that so you can figure out the right size
		# "hypothetical" principal needed to pay interest on to reach the future value
	pmt = r * p / (1 - (1 + r)**-n)
	return pmt