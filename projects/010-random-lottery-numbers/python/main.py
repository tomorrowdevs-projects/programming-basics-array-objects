import random

extracted_numbers = random.sample(range(49), 6)
extracted_numbers.sort()

for number in extracted_numbers:
    print(number)