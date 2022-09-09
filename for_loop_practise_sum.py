def main():
	one_divided_odd()
	one_divided_even()
	odd_divided_even()
	even_divided_odd()

def one_divided_odd():
	print("\nOne divided by odd fractions")
	print("----------")

	denominator = 0

	for i in range(3,100):
		if i % 2 == 0:
			continue
		denominator += 1/i

	S = 1/denominator
	S = round(S,3)

	print("Sum = " + str(S))

def one_divided_even():
	print("\nOne divided by even fractions")
	print("----------")

	denominator_1 = 0

	for j in range(2,101):
		if j % 2 == 1:
			continue
		denominator_1 += 1/j

	S_1 = 1/denominator_1
	S_1 = round(S_1,3)

	print("Sum = " + str(S_1))

def odd_divided_even():
	print("\nOdd fractions divided by even fractions")
	print("----------")

	numerator_2 = 0
	denominator_2 = 0

	for m in range(3,100):
		if m % 2 == 1:
			continue
		numerator_2 += 1/m

	for n in range(2,101):
		if n % 2 == 0:
			continue
		denominator_2 += 1/n

	S_2 = numerator_2/denominator_2 
	S_2 = round(S_2,3)

	print("Sum = " + str(S_2))

def even_divided_odd():
	print("\nEven fractions divided by odd fractions")
	print("----------")

	numerator_3 = 0
	denominator_3 = 0

	for u in range(2,101):
		if u % 2 == 1:
			continue
		numerator_3 += 1/u

	for v in range(3,100):
		if v % 2 == 0:
			continue
		denominator_3 += 1/v

	S_3 = numerator_3/denominator_3
	S_3 = round(S_3,3)

	print("Sum = " + str(S_3))

main()