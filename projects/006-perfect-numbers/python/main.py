def proper_divisors(n):
	divisors=list()
	for i in range(1,n):
		if n%i==0:
			divisors.append(i)
	return divisors

def perfect_number(n):
	divisors=proper_divisors(n)
	divisors_sum=0
	for i in divisors:
		divisors_sum+=i
	if divisors_sum==n:
		return True
	else:
		return False	

def main():
	for n in range(1,10000):
		if perfect_number(n):
			print(n)

if __name__=="__main__":
	main()