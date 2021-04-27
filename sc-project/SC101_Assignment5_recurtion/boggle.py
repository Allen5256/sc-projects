"""
File: boggle.py
Name: Allen Lee
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


# Global variables
dictionary = {}


def main():
	"""
	TODO:
	"""
	read_dictionary()
	num = 0
	letter_lst = []
	ans_lst = []
	ans = ''
	ch_index_lst = []
	current_index = ()
	while True:
		num += 1
		row = input(f'{num} row of letters: ')
		row = row.lower()
		row_without_blank = []
		for ch in row:
			if ch != ' ':
				row_without_blank.append(ch)
		letter_lst.append(row_without_blank)
		if len(row) != 7 or len(row_without_blank) != 4:
			print('Illegal input')
			break
		if num == 4:
			# main function
			boggle(letter_lst, ans_lst, ans, ch_index_lst, current_index)
			print(f'There are {len(ans_lst)} words in total.')
			break


def boggle(letter_lst, ans_lst, ans, ch_index_lst, current_index):
	# Base case
	if ans in dictionary and ans not in ans_lst:
		print(f'Found: "{ans}"')
		ans_lst.append(ans)
	else:
		for i in range(len(letter_lst)):
			for j in range(len(letter_lst[i])):

				# First letter
				if len(ans) == 0:
					ch = letter_lst[i][j]
					ans += ch
					ch_index_lst.append((i, j))

					# Explore from first letter
					if has_prefix(ans):
						boggle(letter_lst, ans_lst, ans, ch_index_lst, current_index=(i, j))

						# Un-choose first letter
						ans = ans[:-1]
						ch_index_lst.pop()
					else:
						ans = ans[:-1]
						ch_index_lst.pop()

				# Choose
				elif current_index == (i, j):
					neighbor_indexes = get_neighbors(i, j, letter_lst)
					for index in neighbor_indexes:
						if index not in ch_index_lst:
							ch = letter_lst[index[0]][index[1]]
							ans += ch
							ch_index_lst.append(index)

							# Explore
							if has_prefix(ans):
								boggle(letter_lst, ans_lst, ans, ch_index_lst, current_index=index)
								if count_prefixes(ans) > 1:
									boggle(letter_lst, ans_lst, ans, ch_index_lst, current_index=index)

								# Un-choose
								ans = ans[:-1]
								ch_index_lst.pop()
							else:
								ans = ans[:-1]
								ch_index_lst.pop()
						else:
							pass


def get_neighbors(i, j, letter_lst):
	valid_indexes = []
	for x in range(-1, 2):
		for y in range(-1, 2):
			if 0 <= i+x < len(letter_lst) and 0 <= j+y < len(letter_lst[i]):
				valid_indexes.append((i+x, j+y))
	return valid_indexes


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary
	with open(FILE, 'r') as f:
		for line in f:
			if len(line.strip()) >= 4:
				dictionary[line.strip()] = [line.strip()]


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


def count_prefixes(sub_s):
	count = 0
	for word in dictionary:
		if word.startswith(sub_s):
			count += 1
	return count


if __name__ == '__main__':
	main()
