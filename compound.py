def Summary(savings, contributing, value):
	print("=_=_=_=_=_=_=_=")
	print("=_= SUMMARY =_=")
	print("=_=_=_=_=_=_=_=")
	print("Contribution :", savings * contributing,"$")
	print("Final value  :", int(value),"$")
	print("Profit made  :", int(value - (savings * contributing)),"$")

def ShowGrowth(year, value):
	year_string = str(year + 1)
	value_string = str(int(value))
	print("Year "+year_string+" : "+value_string+" $")

def Calculate(interest, savings, contributing, duration):
	value = 0
	for year in range(duration):
		if (year <= contributing):
			value += savings
			value *= interest

		if (year > contributing):
			value *= interest

		ShowGrowth(year, value)
	return value

if __name__ == "__main__":
	interest 		= int(input("Enter the yearly interest % : ")) /100 + 1
	savings 		= int(input("Enter your yearly contribution : "))
	contributing	= int(input("Enter the amount of years contributing : "))
	duration		= int(input("Enter the duration : "))

	value = Calculate(interest, savings, contributing, duration)

	Summary(savings, contributing, value)