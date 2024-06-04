def proper_divisors(n):
	divisors=list()
	for i in range(1,n+1):
		if n%i==0:
			divisors.append(i)
	return divisors

def main():
	n=input('Enter an integer:')
	while not n.isdecimal:
		n=input('Enter an integer:')
	n=int(n)
	divisors=proper_divisors(n)
	print(divisors)

if __name__=="__main__":
	main()