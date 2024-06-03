def outliers(numbers,outliers_number):
	numbers_ordered=numbers.copy()
	numbers_ordered.sort()
	numbers_filtered=numbers_ordered[outliers_number+1:len(numbers_ordered)-outliers_number+1]
	return numbers_filtered
	
def main():
	numbers=list()
	number=input('Enter the list of numbers you want to filter one number at time (blanck input to end the input):')
	while number!='':
		if number.isnumeric:
			numbers.append(number)
			number=input('Enter the list of numbers you want to filter one number at time (blanck input to end the input):')
		else:
			number=input('Only numeric inputs. Retry (blanck input to end the input):')
	if len(numbers)<4:
		print('You have to enter at least 4 values: retry.')
		return
			
	numbers_filtered=outliers(numbers,2)
	outlier=list()
	for number in numbers:
			if number in numbers_filtered:
				pass
			else:
				outlier.append(number)
	print('Your input is: {}'.format(numbers))
	print('The outliers are: {}'.format(outlier))

if __name__=='__main__':
		main()	