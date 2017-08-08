from model.mortgage_models import MthAmort, Mortgage
from views import View

class Controller:
	def __init__(self):
		self.view = View()
		#self.mortgage = None

	def calc_schedule(mortgage):
		
		amort = MthAmort(mortgage)
		
		for mth in range(1, mortgage.term*12 + 1):
			monthly_numbers = amort.calc_period(mth)

		
			self.view.print_amort(monthly_numbers)




def main():
	
	print("Let's calculate your mortgage amortization")
	principal = input("What's the principal amount of the loan? ")
	rate = input("What's the annual interest rate of your loan? ")
	term = input("What's the term, in years, of your loan? ")

	
	controller = Controller()
	
	controller.calc_schedule(Mortgage(principal, rate, term))



if __name__ == '__main__':
	main()