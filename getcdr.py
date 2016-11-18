#!/usr/bin/python3

import sys

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
	if check_init_args():
		return sys.argv[1]

def main():
#	print(len(sys.argv), sys.argv)

	number = get_the_number()

#	print (number)

#    f = open("pbxlog.20161109.Транзитка.blg")
#    for line in f:
#        print(line, end='')

if __name__ == '__main__':
    main()
