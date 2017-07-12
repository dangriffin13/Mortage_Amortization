

class Controller:
	def __init__(self):
		pass


controller = Controller()
print("Let's calculate your mortgage amortization")
principal = input("What's the principal amount of the loan?")
rate = input("What's the annual interest rate of your loan?")
term = input("What's the term, in years, of your loan?")
controller.calculate_mortgage(principal, rate, term)