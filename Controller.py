from model.mortgage_models import MthAmort, Mortgage
from views import View
import matplotlib.pyplot as plt


class Controller:
	def __init__(self):
		self.view = View()
		#self.mortgage = None

	def gather_inputs(self):
		print("Let's calculate your mortgage amortization")
		principal = input("What's the principal amount of the loan? ")
		rate = input("What's the annual interest rate of your loan? ")
		term = input("What's the term, in years, of your loan? ")
		return (principal, rate, term)


	#def calc_schedule(self, mortgage):
		
		#amort = MthAmort(mortgage)
		#print('Monthly Payment ', amort.pmt)

		#schedule = {}
		#for mth in range(1, mortgage.term*12 + 1):
			#onthly_numbers = amort.calc_period(mth)
			#schedule['mth'] = monthly_numbersamort
		
			#self.view.print_amort(monthly_numbers)

		



def main():
	
	controller = Controller()
	mortgage = Mortgage(*controller.gather_inputs())
	amort = mortgage.calc_schedule()

	#for mth in amort.monthly_numbers:
		#print(amort.monthly_numbers[mth])

	#using View
	#for key in amort.monthly_numbers:
		#self.view.print_amort(monthly_numbers)

	#matplotlib pyplot practice	
	mths = sorted(amort.monthly_numbers)

	plt.plot(mths, [amort.monthly_numbers[mth]['Remaining Balance'] for mth in mths], 'g--', 
			 mths, [amort.monthly_numbers[mth]['Cumulative Principal Payments'] for mth in mths], 'y--', 
			 mths, [amort.monthly_numbers[mth]['Cumulative Interest Payments'] for mth in mths], 'r--', 
			 mths, [amort.monthly_numbers[mth]['Cumulative Total Payments'] for mth in mths], 'k--'
			 )
	
	plt.legend(['Remaining Balance','Cumulative Principal Payments','Cumulative Interest Payments','Cumulative Total Payments'],
			   loc='upper center')

	plt.xlabel('Payment Month')

	plt.show()



	



if __name__ == '__main__':
	main()