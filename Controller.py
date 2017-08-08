from model.mortgage_models import MthAmort, Mortgage
from view import View

class Controller:
	def __init__(self):
		self.view = View()
		self.mortgage = None

	def calc_schedule(mortgage):
		for mth in range(mortgage.term*12)
		amort = MthAmort()

		for period in amort:
			self.view.print_amort(period)




def main():
	
	print("Let's calculate your mortgage amortization")
	principal = input("What's the principal amount of the loan?")
	rate = input("What's the annual interest rate of your loan?")
	term = input("What's the term, in years, of your loan?")

	
	controller = Controller()
	controller.mortgage = Mortgage(principal, rate, term)



if __name__ == '__main__':
	main()