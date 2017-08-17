
class Mortgage:
	def __init__(self, principal, rate, term):
		self.principal = float(principal)
		self.rate = float(rate)
		self.term = int(term)

	def calc_schedule(self):
		
		amort = MthAmort(self)

		for mth in range(1, self.term*12 + 1):
			amort.calc_period(mth)

		return amort


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
		self.monthly_numbers[period] = {
		'Month' : period,
		'Principal Payment': self.principal_paydown(),
		'Interest Payment': self.interest_size(),
		'Cumulative Principal Payments': self.recalc_cum_prin(),
		'Cumulative Interest Payments': self.recalc_cum_int(),
		'Cumulative Total Payments' : self.recalc_cum_pmt(),
		'Remaining Balance' : self.recalc_principal()
		}
		
		return self.monthly_numbers[period]

	def interest_size(self):
		interest = self.bal * self.rate
		return interest

	def principal_paydown(self):
		paydown = self.pmt - (self.bal * self.rate)	
		return paydown

	def recalc_cum_prin(self):
		self.prin_cum += self.principal_paydown() # += self.monthly_numbers['Prinicpal Payment']
		return self.prin_cum

	def recalc_cum_int(self):
		self.int_cum += self.interest_size() # += self.monthly_numbers['Interest Payment']
		return self.int_cum

	def recalc_cum_pmt(self):
		self.pmt_cum += self.pmt
		return self.pmt_cum

	def recalc_principal(self):
		self.bal -= self.principal_paydown()
		return self.bal


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