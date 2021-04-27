"""
File: coin_flip_runs.py
Name: Allen Lee
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random


def main():
	"""
	TODO:
	"""
	print('Let\'s flip a coin!')
	num_run = int(input('Number of runs: '))
	result = ''
	count = 0
	is_in_a_run = False
	flip1 = random.randint(0, 1)
	if flip1 == 0:
		result += 'T'
	elif flip1 == 1:
		result += 'H'
	while True:
		if count == num_run:
			break
		flip2 = random.randint(0, 1)
		if flip2 == 0:
			result += 'T'
		elif flip2 == 1:
			result += 'H'
		if flip1 == flip2 and not is_in_a_run:
			count += 1
			is_in_a_run = True
		elif flip1 != flip2:
			is_in_a_run = False
		flip1 = flip2
	print(result)


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
