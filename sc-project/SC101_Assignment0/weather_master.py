"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


EXIT = -100


def main():
	"""
	The program will firstly assign a variable temperature to get user input,
	and then assign both highest and lowest to store the temperature which is from user input.
	Use if and elif to make either highest or lowest change when a new temperature is entered by users.

	To print the number of cold day, a variable cold_day is assigned to store 0 initially,
	and then use another if statement
	to make the number of cold day plus 1 when a new temperature lower than 16 is entered by users.

	To compute the average of all data, both variables data_summary and data_number are assigned to store 0 initially,
	and then when the program runs through while loop once,
	the number of data plus 1 and the summary of data plus the new temperature entered by users.
	Finally, a variable average is assigned to store the result of data_number dividing data summary.
	"""
	print('stanCode "Weather Mater 4.0"!')
	temperature = int(input('Next Temperature: (or -100 to quit)? '))
	highest = temperature
	lowest = temperature
	data_summary = 0
	data_number = 0
	cold_day = 0
	if temperature == EXIT:
		print('No temperatures were entered.')
	else:
		while True:
			if temperature == EXIT:
				break
			elif temperature > highest:
				highest = temperature
			elif temperature < lowest:
				lowest = temperature
			if temperature < 16:
				cold_day += 1
			data_summary += temperature
			data_number += 1
			temperature = int(input('Next Temperature: (or -100 to quit)? '))
		average = data_summary/data_number
		print('Highest Temperature = '+str(highest))
		print('Lowest Temperature = '+str(lowest))
		print('Average = '+str(average))
		print(str(cold_day)+' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
