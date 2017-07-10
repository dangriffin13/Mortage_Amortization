
class MthAmort:
	def __init__(self, 
				payment,
				principal_payment,
				interest_payment,
				remaining_balance,
				cumulative_principal_payment,
				cumulative_interest_payment,
				cumulative_total_payment
				):
		self.pmt = payment
		self.prin_pmt = principal_payment
		self.int_pmt = interest_payment
		self.bal = remaining_balance
		self.prin_cum = cumulative_principal_payment
		self.int_cum = cumulative_interest_payment
		self.pmt_cum = cumulative_total_payment
