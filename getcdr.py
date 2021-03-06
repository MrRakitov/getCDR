#!/usr/bin/python3

#to use the command string arguments
import sys

#to use directory listing
import os

#to use the regular expression
import re

#GLOBAL variables
#Length of the number to find
NUMBER_LENGTH = 6
#file name regular expression
FILE_REGEX = r"\.blg"

#check the length of the number
def check_num_len(num, num_len):
	'''Returns TRUE if length of the num equals num_len. Returns False otherwise'''

	return True if len(num) == num_len else False

def check_init_args():
	"""Summary
		Returns True if number of command line arguments is correct
		otherwise stop running the program.
	Returns:
	    TYPE: bool
	"""
	if len(sys.argv) < 2:
		sys.exit("At least one argument is need\nUSAGE: {} <phone Number>".format(sys.argv[0]))
	elif len(sys.argv) > 2:
		sys.exit("Too many arguments\nUSAGE: {} <phone Number>".format(sys.argv[0]))
	else:
		return True

def get_the_number():
	"""Get the number from command line
	Returns:
	    TYPE: str
	"""
	if check_init_args():
		num = sys.argv[1]
		return num if check_num_len (num, NUMBER_LENGTH) else False

def open_in_file(filename):
	"""Trying to open a file.
	Returns: A file handler if OK or False if something wrong
	"""
	try:
		f = open(filename, 'r')
		return f
	except:
		print("Oops! something wrong with opening file")
		return False

def print_file(file, number):
	"""Print content of the file
	Input: File handler
	Returns: nothing
	"""
	entry_counter = 0
	regex = r"[ ]" + str(number)
	for line in file:
		if re.search(regex, line):
			print(line, end='')
			entry_counter += 1
	return entry_counter

def proceed(number):
	entrys = 0
	for filename in get_files_list():
		file = open_in_file(filename)
		result = print_file(file, number)
		if result > 0:
			entrys += result
	print('{} entry(s) found'.format(entrys))
	return True

def get_files_list():
	'''Read all files with FILE_REGEX mask in current directory
	Returns: list of file names
	'''
	files = os.listdir(os.curdir)
	files_list = []
	for file in files:
		if re.search(FILE_REGEX, file):
			files_list.append(file)
	return files_list


def main():
	#Get the number to find
	number = get_the_number()
	if number != False:
		proceed(number)
	else:
		print("Number must be {} digits long".format(NUMBER_LENGTH))

if __name__ == '__main__':
    main()
