
class Mortgage:
	def __init__(self, principal, rate, term):
		self.principal = principal
		self.rate = rate
		self.term = term


class MthAmort:
	def __init__(self, mortgage): #a mortgage object is passed in
		self.bal = mortgage.principal
		self.rate = mortgage.rate/12/100
		self.pmt = payment_size(mortgage.principal, mortgage.rate, mortgage.term * 12)
		#self.prin_pmt = 0
		#self.int_pmt = 0
		self.prin_cum = 0
		self.int_cum = 0
		self.pmt_cum = 0
		self.monthly_numbers = {}

	def calc_period(self, period):
		self.monthly_numbers['Month'] = period
		self.monthly_numbers['Principal Payment'] = principal_paydown(self.bal, self.pmt, self.rate)
		self.monthly_numbers['Interest Payment'] = interest_size(self.bal, self.rate)
		self.monthly_numbers['Cumulative Principal Payments'] = self.recalc_cum_prin(self)
		self.monthly_numbers['Cumulative Interest Payments'] = self.recalc_cum_int(self)
		self.monthly_numbers['Cumulative Total Payments'] = self.recalc_cum_pmt(self)
		self.monthly_numbers['Remaining Balance'] = recalc_principal(self)
		return self.monthly_numbers

	def interest_size(remaining_balance, rate):
		interest = remaining_balance * rate
		return interest

	def principal_paydown(remaining_balance, payment, rate):
		paydown = payment - (remaining_balance * rate)	
		return paydown

	def recalc_principal(self):
		self.bal -= self.bal - principal_paydown(self.bal, self.pmt, self.rate)
		return remaining_balance

	def recalc_cum_prin(self):
		self.prin_cum += principal_paydown(self.bal, self.pmt, self.rate)
		return self.prin_cum

	def recalc_cum_int(self):
		self.int_cum += interest_size(self.bal, self.rate)
		return self.int_cum

	def recalc_cum_pmt(self):
		self.pmt_cum += self.bal * self.rate
		return self.pmt_cum


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